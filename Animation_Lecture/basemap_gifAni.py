#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
__author__ = 'James T. Dietrich'
__contact__ = 'james.t.dietrich@dartmouth.edu'
__copyright__ = '(c) James Dietrich 2016'
__license__ = 'MIT'
__date__ = 'Thu Feb 23 15:07:09 2017'
__version__ = '1.0'
__status__ = "initial release"
__url__ = "https://github.com/geojames/..."

"""
Name:           __name__.py
Compatibility:  Python 3.5
Description:    This program does stuff

URL:            https://github.com/geojames/...

Requires:       libraries

Dev ToDo:       

AUTHOR:         James T. Dietrich
ORGANIZATION:   Dartmouth College
Contact:        james.t.dietrich@dartmouth.edu
Copyright:      (c) James Dietrich 2017

"""
#------------------------------------------------------------------------------
# Imports
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

# MAIN
# get data

# read in excel sheets as pandas dataframes
city_pop = pd.read_excel('US_metro_area_population_1790_2010.xls', sheetname='metro_data_to_pandas') 
years = pd.unique(city_pop.year)

duration = 11.5   # length of movie in sections
fps = 2

# Set up plot outside of function that will make the slides 
fig, ax = plt.subplots(1,figsize=(9,7.75),facecolor='white')
ax.set_title('20 Largest Metro Regions in 2010')
m = Basemap(width=6000000,height=4500000,projection='lcc',
            resolution='l',lat_1=45.,lat_2=55,lat_0=40,lon_0=-97.)
m.drawcoastlines()
m.drawcountries()

# image file list
keyFrames = []

for idx,year in enumerate(years):
    ax.set_title(year)
    year_pop = city_pop[(city_pop.year == year)]
    lons = year_pop.lon.values
    lats = year_pop.lat.values
    xm,ym = m(lons,lats)
    marker_size = np.sqrt(year_pop.population.values)
    plt_handle = m.scatter(xm,ym,marker_size,marker='o',facecolor='r', edgecolor='k', alpha=0.5)
    #plt.show()
    filename = "popMap" + str(idx) + ".png"
    plt.savefig(filename)
    keyFrames.append(filename)
    plt_handle.remove()

im = Image.open(keyFrames[0])
images = [Image.open(fn) for fn in keyFrames]
gifFilename = "Pop_Map_Ani.gif"

# https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html#saving
im.save(gifFilename, format='gif', save_all = True, duration = 500, loop = 3, append_images = images)
