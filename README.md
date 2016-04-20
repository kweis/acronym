## Automatic ARCTIC reductions
Kolby Weisenburger

2016

Automatic reduction pipeline for the Astrophysical Research Consortium Telescope Imaging Camera ([ARCTIC](http://www.apo.nmsu.edu/arc35m/Instruments/ARCTIC/)) at Apache Point Observatory ([APO](http://www.apo.nmsu.edu/)).


to use:

**python reduce_arctic.py [your directory of data]**

OR place .py in your folder with data and run with no argument:

**python reduce_arctic.py**

creates [your directory]/reduced/cals/ and [your directory]/reduced/data/



  ```bash
04:50:00 $ python reduce_arctic.py /Users/kolbylyn/Desktop/UT02072016/Q1UW02/UT160209

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
