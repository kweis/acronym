## Automatic ARCTIC reductions
Kolby Weisenburger

2016

Automatic reduction pipeline for the Astrophysical Research Consortium Telescope Imaging Camera ([ARCTIC](http://www.apo.nmsu.edu/arc35m/Instruments/ARCTIC/)) at Apache Point Observatory ([APO](http://www.apo.nmsu.edu/)).

<img src="https://github.com/kweis/acronym/blob/master/docs/Aligned_m106.png" width="500" height="500" align="middle"/>

to use:

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
