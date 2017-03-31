
# coding: utf-8

"""
acronym.py
Kolby Weisenburger, Joseph Huehnerhoff, Emily Levesque, Phil Massey
kweis@uw.edu
2016

Automatic reduction pipeline for the Astrophysical Research Consortium Imaging Camera (ARCTIC) at Apache Point Observatory (APO).

to use:
python acronym.py [your directory of data]

OR place .py in your folder with data and run with no argument:
python acronym.py

creates /reduced/cals/ and /reduced/data/

"""

import numpy as np
import glob
import os
import re
import sys
import warnings
import pandas as pd
try:
    import astropy.io.fits as pyfits
except ImportError:
    import pyfits

# ignore overwriting reduced files warnings in case you need to rerun
warnings.filterwarnings('ignore', message='Overwriting existing file')

# take directory from user or assume current directory
if len(sys.argv) > 1:
    direc = sys.argv[1]
else:
    direc = '.'

# directories for reduced images
if not os.path.exists(direc+'/reduced/cals'):
    os.makedirs(os.path.join(direc, 'reduced/cals'))
if not os.path.exists(direc+'/reduced/data'):
    os.makedirs(os.path.join(direc, 'reduced/data'))

# grab all files from the directory; organize dataframe
files = glob.glob(direc+"/*.fits")

df = pd.DataFrame(files,columns=['fname'])
df['objtype'] = pd.Series("", index=df.index)
df['filt'] = pd.Series("", index=df.index)
df['exp'] = pd.Series("", index=df.index)
df['objname'] = pd.Series("", index=df.index)

for ff,fname in enumerate(files):
    try:
        df['objtype'][ff] = pyfits.open(fname)[0].header['IMAGETYP']
        df['filt'][ff] = pyfits.open(fname)[0].header['FILTER']
        df['exp'][ff] = pyfits.open(fname)[0].header['EXPTIME']
        df['objname'][ff] = pyfits.open(fname)[0].header['OBJNAME']
    except IOError:    
        print('\n File corrupt or missing: ' + fname)


# ARCTIC reads out images in various ways. check headers for quad or LL (lower left) mode and trim respectively        
def trim_image(f):
    datfile = pyfits.getdata(f, header=True)
    dat_raw = datfile[0]
    dat_head = datfile[1]
    
    amp = pyfits.open(f)[0].header['READAMPS']
    
    if amp == "Quad":
        # ll, ul, lr, ur
        quads = ['DSEC11', 'DSEC21', 'DSEC12', 'DSEC22']

        dat = [[],[],[],[]]
        for i,quad in enumerate(quads):
            idx_string = pyfits.open(f)[0].header[quad]
            idx = re.split('[: ,]',idx_string.rstrip(']').lstrip('['))
            dat[i] = dat_raw[int(idx[2]):int(idx[3]),int(idx[0]):int(idx[1])]
    
        sci_lo = np.concatenate((dat[2], dat[3]), axis = 1)
        sci_up = np.concatenate((dat[0], dat[1]), axis = 1)
        sci = np.concatenate((sci_up, sci_lo), axis = 0)
    
    if amp == 'LL':
        idx_string = pyfits.open(f)[0].header['DSEC11']
        idx = re.split('[: ,]',idx_string.rstrip(']').lstrip('['))
        sci = dat_raw[int(idx[2]):int(idx[3]),int(idx[0]):int(idx[1])]
    
    return [sci,dat_head]



# given an exposure time, go get that dark or scale down from longest dark. 
def getdark(expt):
    try:
        dark = pyfits.getdata(direc+'/reduced/cals/master_dark_'+str(expt)+'.fits')
    except IOError:
        scaleto = np.max(df['exp'][df['exp'] != ''])
        dark = pyfits.getdata(direc+'/reduced/cals/master_dark_'+str(scaleto)+'.fits')
        dark *= (expt/scaleto)
    return dark



### CREATE MASTER BIAS #######################################

print('\n >>> Starting bias combine...')

bias_idx = df[df['objtype'] == 'Bias'].index.tolist()
if len(bias_idx) == 0:
    print('   > No biases found. Continuing reductions...')
    bias=0.
else:
    biases = np.array([trim_image(df['fname'][n])[0] for n in bias_idx])
    bias = np.median(biases,axis=0)
    pyfits.writeto(direc+'/reduced/cals/master_bias.fits',bias,overwrite=True)
    print('   > Created master bias')



### CREATE MASTER DARKS ######################################
### these are bias subtracted

# array of all exposure times found
times = list(filter(None,pd.unique(df.exp.ravel())))

print('\n >>> Starting darks...')

for ii in range(0,len(times)):
    dark_idx = df[(df['exp'] == times[ii]) & (df['objtype'] == 'Dark')].index.tolist()
    if len(dark_idx) == 0:
        print('   > No darks found for exposure time ' + str(times[ii]) + ' sec. Continuing reductions...')
    else:
        darks = np.array([trim_image(df['fname'][n])[0] for n in dark_idx]) - bias
        dark_final = np.median(darks,axis=0)
    
        name = direc+'/reduced/cals/master_dark_'+str(times[ii])+'.fits'
        pyfits.writeto(name,dark_final,overwrite=True)
        print('   > Created master '+ str(times[ii])+' second dark')



### CREATE MASTER FLATS ######################################
### these are bias and dark subtracted then normalized

# array of all filters found
filters = list(filter(None,pd.unique(df.filt.ravel())))

print('\n >>> Starting flats...')

for ii in range(0,len(filters)):
    flat_idx = df[(df['filt'] == filters[ii]) & (df['objtype'] == 'Flat')].index.tolist()
    
    if len(flat_idx) == 0:
        print('   > No flats found for the ' + str(filters[ii]) + ' filter. Continuing reductions...')
    else:
        # get the correct master dark. if not exact exp time, scale it
        # from the longest dark frame. if no darks at all, continue.
        expt = df['exp'][flat_idx[0]]
        try:
            dark = getdark(expt)
        except IOError:
            dark = 0.
        
        flats = np.array([trim_image(df['fname'][n])[0] for n in flat_idx]) - bias - dark
        flat_final = np.median(flats,axis=0)
        flat_final /= np.max(flat_final)

        filts = filters[ii][-1]
        name = direc+'/reduced/cals/master_flat_'+filts+'.fits'
        pyfits.writeto(name,flat_final,overwrite=True)
        print('   > Created master '+ str(filters[ii])+' flat')



### REDUCE SCIENCE IMAGES ####################################
# (science_raw - dark) / masterflat

dat_idx = df[df['objtype'] == 'Object'].index.tolist()

print('\n >>> '+str(len(dat_idx))+' science images found. Starting reductions...')
for n in dat_idx:
    datfile = trim_image(df['fname'][n])
    dat_raw = datfile[0]
    dat_head = datfile[1]
    
    time = df['exp'][n]
    try:
        dark = getdark(time)
    except IOError:
        dark = 0.
    
    filt = (df['filt'][n])[-1]
    try:
        flat = pyfits.getdata(direc+'/reduced/cals/master_flat_'+str(filt)+'.fits')
    except IOError:
        print('   > Warning! No ' + str(df['filt'][n]) + ' filter flat found for ' + df['fname'][n])
        flat = 1.
        
    dat = (dat_raw - dark) / flat
    name = os.path.join(direc, 'reduced/data', 'red_'+os.path.basename(df['fname'][n]))
    pyfits.writeto(name,dat,overwrite=True,header=dat_head)

print('\n >>> Finished reductions! \n')
