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
Name:           Week5-1_DataImport.py
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

# !!!!!!!!!!!!!!!
#
#   Before we begin...
#   you must create a standardized places for all of your code and the data
#   I suggest a new folder in your "documents" folder called Python
#       ON PC: C:\users\<your name>\Documents\Python
#       ON MAC: /Users/<your name>/Documents/Python
#
#   Inside that folder you can start new folders for different labs/projects
#       For this exercise, create a folder called: DataIO
#
# !!!!!!!!!!!!!!!

#%% IMPORTING DATA with CSV Library

import os
import csv
from datetime import datetime

# Change the current working directory to our Data folder
# WINDOWS
os.chdir("C:/Users/James//Documents/GitHub/Dart_EnvGIS/Data/")

# MAC
os.chdir("/Users/ryanmckeon/GitHub/Dart_EnvGIS/Data/")

# These are programatic calls that will work when running a script.  If you
# are just typing into the console you can use Unix commands directly without
# calling the OS library... ex: cd /Users/ryanmckeon/Documents/pyhton


# create blank lists to hold the data
dates = []
flows = []

# Opens file as read only. csv.reader reads each line in the file and
# automatically creates a LIST of each row in the file
# the indicies in the list correspond to the values in between the commas
#   in Lees_Ferry_short.csv, the values for each line are date and flow
#   2015-01-01,12800
#
# OK for known inputs with known length
#   Literally interprets data as strings, so conversion is nessesary

with open("Lees_Ferry_flow_Short_no_header.csv","r") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        dates.append(row[0])    # dates.append(datetime.strptime(row[0],"%Y-%M-%d"))
        flows.append(row[1])    # flows.append(float(row[1]))

# type conversion (inline conversions above)
date_conv = []
flows_conv = []

for val in dates:
    date_conv.append(datetime.strptime(val,"%m/%d/%y"))

for flow in flows:
    flows_conv.append(float(flow))

#%% IMPORTING DATA with Numpy loadtxt

# Numpy's loadtxt function looks for TAB delimiters and a header row with a # sign
# for the population.txt sample file:
#       #year  hare    lynx    carrot
#       1900    30e3    4e3     48300
#       1901    47.2e3  6.1e3   48200
#
# loadtxt will create a 2-D array of the data in the txt file
#   it's slightly stupid and will load everything as one data type
#   *** i.e. the first datatype it encounters
# You could separate the columns to individual 1-D arrays and switch
# the datatypes after import

import os
import numpy as np

data = np.loadtxt('populations.txt')


#%% IMPORTING DATA with Numpy genfromtxt

# genfromtxt gives more options for importing different data types
# see the documentation for all fo the options:
#  http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.genfromtxt.html
#
# you can specifiy a delimiter, data types, and basic names for the data in the
# array
# If you use the names=True option it will create a structured array where we
#   can handle different data types

import os
import numpy as np

data2 = np.genfromtxt('populations_w_names.txt',delimiter="\t", names=True)


#%% IMPORTING DATA with Pandas
#
# Pandas offers the easiest way to import data from a variety of file formats
#   read_table - reads tab delimited files
#   read_csv   - reads comma delimited files
#   read_excel - reads excel files/tables
#
# The outputs will be in a Pandas data frame
# for read_csv Pandas will do it's best to guess data types
# There are lot's on options for this function:
#   http://pandas.pydata.org/pandas-docs/stable/io.html#io-read-csv-table

import os
import pandas as pd

# weather data  
weather = pd.read_csv("KVTNORWI2_2016-12-1_2017-01-26.csv")

# Trying our Stream Flow data again
flow_data = pd.read_csv("Lees_Ferry_flow_Short.csv")

#%% parsing dates/times with PANDAS

import os
import pandas as pd

weather_date = pd.read_csv("KVTNORWI2_2016-12-1_2017-01-26.csv", parse_dates=["Time"])
flow_data_date = pd.read_csv("Lees_Ferry_flow_Short.csv", parse_dates=["date"])

# or using column indeices

weather = pd.read_csv("KVTNORWI2_2016-12-1_2017-01-26.csv", parse_dates=[0])

#%% Cheaters file paths

# Not working well on a Mac -- Ryan

# the libaray Tkinter is a GUI (graphical user interface) that can be used to
#   build entire GUI applications. But there is a quick and easy file picker
#   that we can use to choose a file easily and like you're used to in
#   other applications. The window just


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

target_file = fd.askopenfilename(title='Open a file',
                                 filetypes=[('Comma-Delimited Files (*.csv)',
                                 '*.csv')],initialdir=os.getcwd())

print(target_file)

data = pd.read_csv(target_file)

# clean up the tkinter app
app.destroy()
