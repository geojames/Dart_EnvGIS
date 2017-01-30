#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
__author__ = 'James T. Dietrich'
__contact__ = 'james.t.dietrich@dartmouth.edu'
__copyright__ = '(c) James Dietrich 2016'
__license__ = 'MIT'
__date__ = 'Wed Nov 16 11:33:39 2016'
__version__ = '1.0'
__status__ = "initial release"
__url__ = "https://github.com/geojames/..."

"""
Name:           Week5-1_DataExport.py
Compatibility:  Python 3.5
Description:    This program does stuff

URL:            https://github.com/geojames/...

Requires:       libraries

Dev ToDo:

AUTHOR:         James T. Dietrich
ORGANIZATION:   Dartmouth College
Contact:        james.t.dietrich@dartmouth.edu
Copyright:      (c) James Dietrich 2016

"""
#------------------------------------------------------------------------------

#%%

# you can also use the "cheaters" file path Tkinter code from the Data Import
# file to geenrate a file path to save a file...

import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog as fd

# start tkinter for file choosing
app = tk.Tk()

# use the file dialog call to get a file name
#   Options:
#       title - text at the top of the window
#       file types - filter for specific file types
#       initialdir - the starting directory
#       defaultextension - will automatically add this extention if not present

outfile = fd.asksaveasfilename(title='Save Corrected Poitns As...',
                                 filetypes=[('Comma-Delimited Files (*.csv)',
                                 '*.csv')],initialdir=os.getcwd(),
                                 defaultextension='.csv')

print(outfile)

# clean up the tkinter app
app.destroy()

# EXPORT CODE...using outfile at the file path...


#%% File Output with the CSV library

import os
import csv
import random as rand

# create an objectID list
OID = list(range(0,11))

# blank lists
lat = []
lon = []
elev = []

# Create random latitude, longitude, and elevation values
for num in range(0,11):
    lat.append(rand.uniform( 35, 45 ))
    lon.append(rand.uniform( -90, -120 ))
    elev.append(rand.uniform( 0, 500 ))

# change the working directory (change this to where you want yoiur output)
#Windows
os.chdir("C:/Users/James//Documents/GitHub/Dart_EnvGIS/Data/")

# MAC
os.chdir("/Users/ryanmckeon/GitHub/Dart_EnvGIS/Data/")

# ** A very useful feature for any export **
# check to see if an Exports folder exists, if not...create one
if os.path.exists("Exports") == False:
    os.mkdir("Exports")

# open a new file in the Exports folder as writable 'w'
#   create a csv writer, write header row
#   for each row in the data lists write the values line by line
with open("Exports\\CSV_export.csv", 'w') as file_out:
    writer = csv.writer(file_out)
    writer.writerow( ("ID", "LAT", "LONG", "elev") )
    for row in range(len(OID)):
        writer.writerow( (OID[row],lat[row],lon[row],elev[row]) )

# close the file
file_out.close()

#%% Exporting with Numpy
#
# The savetxt function outputs a text file, you can specify a delimiter and
#   a format code (like formated print statements)

import os
import numpy as np

# we already did this above...
#os.chdir("C:/Users/James//Documents/GitHub/Dart_EnvGIS/Data/")

if os.path.exists("Exports") == False:
    os.mkdir("Exports")
    
x = np.arange(1.0,11.0)
y = np.random.rand(10,10)

np.savetxt("Exports/Numpy_out_01.csv", y, delimiter=",", fmt="%0.4f")

combine = np.column_stack((x.T,y))

np.savetxt("Exports/Numpy_out_02.csv", combine, delimiter=',', \
            fmt=("%0.4f"), header = "ROW,LOTS OF RANDOS")
            
#%% Exporting with Pandas
#
# Again...easiest of all, Pandas Data Frames have a .to_csv method to export to
# a csv file
            
import os
import pandas as pd

#os.chdir("C:/Users/James//Documents/GitHub/Dart_EnvGIS/Data/")

if os.path.exists("Exports") == False:
    os.mkdir("Exports")

# Read in sample weather data
weather = pd.read_csv("KVTNORWI2_2016-12-1_2017-01-26.csv")

# create a seubset of the weather data frame
weather_subset = weather[['Time','TemperatureC','WindDirection']]

# Output the subset to a new CSV in the Exports folder
weather_subset.to_csv("Exports/pandas_export.csv")

# There are other outputs as well - Excel, JSON, XML, HTML...
#   Here is an excel output:
weather_subset.to_excel("Exports/pandas_export.xlsx")

