## Automatic ARCTIC reductions
Kolby L. Weisenburger, Joseph Huehnerhoff, Emily M. Levesque, Philip Massey

2017

<<<<<<< HEAD
**Acronym** is an automatic reduction pipeline for the Astrophysical Research Consortium Telescope Imaging Camera ([ARCTIC](http://www.apo.nmsu.edu/arc35m/Instruments/ARCTIC/)) at Apache Point Observatory ([APO](http://www.apo.nmsu.edu/)). Despite an increasing number of telescopes and observatories coming online, instrument-specific image reduction packages have been severely lacking. Historically, astronomers have resorted to building in-house (potentially ad-hoc) software to calibrate raw astronomical images; these different reduction algorithms can lead to discrepant scientific results. **Acronym** aims to streamline this image reduction process such that all ARCTIC users can benefit from 1. an open-source and open-access automatic reduction pipeline and 2. a normalized tool so that they are able to compare apples to apples and galaxies to galaxies. 

We developed in-house procedures to reduce ARCTIC images rather than using other similar packages (e.g. [astropy's ccdproc] (https://github.com/astropy/ccdproc), [DOI: 10.5281/zenodo.47652] (https://zenodo.org/record/47652)) to handle ARCTIC's various CCD readout modes. While these unique readout modes could have been enveloped into a helper function and used in tandem with astropy's ccdproc, we wished to maintain a package that was curated specifically for the ARCTIC instrument and that did not rely on preexisting reduction packages.
=======
**Acronym** is an automatic reduction pipeline for the Astrophysical Research Consortium Telescope Imaging Camera ([ARCTIC](http://www.apo.nmsu.edu/arc35m/Instruments/ARCTIC/)) at Apache Point Observatory ([APO](http://www.apo.nmsu.edu/)). Despite an increasing number of telescopes and observatories coming online, instrument-specific image reduction packages have been severely lacking. Historically, astronomers have resorted to building in-house (potentially ad-hoc) software to calibrate raw astronomical images; these different reduction algorithms can lead to discrepant scientific results. **Acronym** aims to streamline this image reduction process such that all ARCTIC users can benefit from 1. an open-source and open-access automatic reduction pipeline and 2. a normalized tool so that they are able to compare apples to apples and galaxies to galaxies. We developed in-house procedures to reduce ARCTIC images rather than using other similar packages (e.g. [astropy's ccdproc] (https://github.com/astropy/ccdproc), [DOI: 10.5281/zenodo.47652] (https://zenodo.org/record/47652)) to handle ARCTIC's various CCD readout modes. While these unique readout modes could have been enveloped into a helper function and used in tandem with astropy's ccdproc, we wished to maintain a package that was curated specifically for the ARCTIC instrument and that did not rely on preexisting reduction packages.
>>>>>>> a99e4bdb7864ad10c2323e1b8f323e65dcd015ca


<img src="https://github.com/kweis/acronym/blob/master/docs/Aligned_m106.png" width="500" height="500" align="middle"/>

_Stacked M106 image using reduced Johnson V, R, and I band images (reduced by **acronym**)._


To use:

**python acronym.py [your directory of data]**

OR place .py in your folder with data and run with no argument:

**python acronym.py**


## Example

You can test the **acronym** pipeline using the /example/rawdata zipfile (example.zip in release docs) or an ARCTIC dataset of your choosing. To verify the results of the reduced example directory, use the test.py script (see below).


Expected output for example directory reduction:

  ```bash
04:51:10 $ python acronym.py example/rawdata

 >>> Starting bias combine...
   > Created master bias

 >>> Starting darks...
   > Created master 10.0 second dark
   > Created master 30.0 second dark
   > Created master 5.0 second dark
   > Created master 60.0 second dark
   > No darks found for exposure time 120.0 sec. Continuing reductions...

 >>> Starting flats...
   > Created master MSSSO R flat
   > Created master MSSSO V flat

 >>> 7 science images found. Starting reductions...

 >>> Finished reductions! 
  ```
  
  This created _example/rawdata/reduced/cals/_ and _example/rawdata/reduced/data/_. In case of missing select calibration (e.g. 30 second darks), **acronym** will alert you, but continue to reduce the other images. 
  
Expected output for test.py in example directory:


  
  

Please contact Kolby Weisenburger (kweis@uw.edu) with questions, issues or contributions. 