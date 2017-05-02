---
title: 'acronym: An Automatic Reduction Pipeline for Astronomical Images'
tags:
  - Python
  - data reduction
  - astronomy
authors:
  - name: Kolby L. Weisenburger
    orcid: 0000-0002-4639-1436
    affiliation: 1
  - name: Joseph Huehnerhoff
    orcid:
    affiliation: 1
  - name: Emily M. Levesque
    orcid:
    affiliation: 1
  - name: Philip Massey
    orcid:
    affiliation: 2
affiliations:
  - name: University of Washington
    index: 1
  - name: Lowell Observatory
    index: 2
date: 23 Oct 2016
bibliography: paper.bib
---

# Summary

Acronym is a Python implementation of an automatic reduction pipeline for the Astrophysical Research Consortium Telescope Imaging Camera (ARCTIC). ARCTIC is an optical-wavelength CCD camera mounted on a 3.5 meter telescope at Apache Point Observatory (APO) in Sunspot, New Mexico. We developed in-house procedures to reduce ARCTIC images rather than using other similar packages (e.g. @ccdproc) to handle ARCTIC's various CCD readout modes.

Given raw ARCTIC images, acronym outputs dark, bias, and flat-corrected images. 

This M106 image is the product of three stacked acronym-reduced images.

-![M106 in all its glory.](Aligned_m106.png)

# References 
