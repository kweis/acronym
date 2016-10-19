## Automatic ARCTIC reductions
Kolby Weisenburger

2016

**Acronym** is an automatic reduction pipeline for the Astrophysical Research Consortium Telescope Imaging Camera ([ARCTIC](http://www.apo.nmsu.edu/arc35m/Instruments/ARCTIC/)) at Apache Point Observatory ([APO](http://www.apo.nmsu.edu/)). Despite an increasing number of telescopes and observatories coming online, instrument-specific image reduction packages have been severely lacking. Historically, astronomers have resorted to building in-house (potentially ad-hoc) software to calibrate raw astronomical images; these different reduction algorithms can lead to discrepant scientific results. **Acronym** aims to streamline this image reduction process such that all ARCTIC users can benefit from 1. an open-source and open-access automatic reduction pipeline and 2. a normalized tool so they're able to compare apples to apples and galaxies to galaxies.

<img src="https://github.com/kweis/acronym/blob/master/docs/Aligned_m106.png" width="500" height="500" align="middle"/>

_Stacked M106 image using reduced Johnson V, R, and I band images (reduced by **acronym**)._


## Example

You can test the **acronym** pipeline using the /example data directory in this repository or an ARCTIC dataset of your choosing.

To use:

**python acronym.py [your directory of data]**

OR place .py in your folder with data and run with no argument:

**python acronym.py**

creates [your directory]/reduced/cals/ and [your directory]/reduced/data/



  ```bash
04:50:00 $ python acronym.py rawdata/

 >>> Starting bias combine...
     > Created master bias

 >>> Starting darks (if you have them)...
     > Created master 10.0 second dark
     > Created master 120.0 second dark
     > Created master 30.0 second dark
     > Created master 300.0 second dark
     > Created master 5.0 second dark
     > Created master 60.0 second dark

 >>> Starting flats...
     > Created master MSSSO R flat
     > Created master MSSSO B flat
     > Created master MSSSO I flat
     > Created master MSSSO U flat
     > Created master MSSSO V flat

 >>> 65 science images found. Starting reductions...
 >>> Finished reductions! 
  ```
