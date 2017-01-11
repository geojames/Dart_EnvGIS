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
Name:           Week2-2_Functions_Libraries.py
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

## WHAT IS A FUNCTION?

#%%

# Built in functions
# https://docs.python.org/3/library/functions.html



#%%

# METHODS

# Specific options/functions for the different data objects

# INT - https://docs.python.org/3.5/library/stdtypes.html#additional-methods-on-integer-types
# FLOAT - https://docs.python.org/3.5/library/stdtypes.html#additional-methods-on-float

# STR - https://docs.python.org/3.5/library/stdtypes.html#string-methods

# LIST - https://docs.python.org/3/tutorial/datastructures.html#more-on-lists


#%%

# PACKAGES / "LIBRARIES"
# Python, and especially Anaconda, come with several pacakges “pre-installed”

# To see what packages you have installed:
# -	On MAC, open Termial
# -	On PC, find the Anaconda Prompt in your Start Menu
#
# -	Type:      conda list
#   o	Within Anaconda, conda is the package manager
#
# -	The default Python package manager is called PIP
#   o	In your terminal: pip list

# Libraries available through PIP (PyPi)
# -	https://pypi.python.org/pypi/
#
# Libraries available through CONDA
# -	http://docs.continuum.io/anaconda/pkg-docs
#
# To install/update a package
#   pip install package_name
#   conda install package_name



# Useful “standard” packages - https://docs.python.org/2/library/
# -	math
# -	random
# -	datetime
# -	calendar
# -	fractions

# OS - access operating system functionality
#   https://docs.python.org/2/library/os.html

import os

# get the current working directory (cwd)
os.getcwd()

# make a new folder in the cwd (make directory)
os.mkdir(“fun_folder”)

# list the folders and files in the cwd
os.listdir(os.curdir)


# list the folders and files in another directory
PC – os.listdir(“C:/”)
MAC – os.listdir(“/”)

# os.path

# get the file path to a file
path = os.path.abspath("temp.py")
print(path)

# get the folder that contains the file
os.path.dirname(path)

# get the file’s “base name”, i.e. the name of the file
os.path.basename(path)

# check to see if a file exists
os.path.exists("temp.py")


#%%

# THE SCIPY FAMILY

# SciPy – http://www.scipy.org/

import scipy as sp

# -	Interpolation (scipy.interpolate)
# -	Statistics (scipy.stats)
# -	Multidimensional image processing (scipy.ndimage)
# -	File IO (scipy.io)

# Numpy - Multidimensional Arrays / Data IO (http://docs.scipy.org/doc/numpy/)

import numpy as np

# Pandas - Data Analysis / Data IO (http://pandas.pydata.org/pandas-docs/stable/)

import pandas as pd

# -	Arrays like Numpy (uses Numpy)
# -	Additional data type called a Data Frame
# -	Time Series analysis

# Matplotlib – 2D and 3D plotting (http://matplotlib.org/)

# -Creating graphs and plots for your data

from matplotlib import pyplot as plt


#%%

# CUSTOM FUNCTIONS
# write your own funtions to reuse code and simplify your code structure

# Cartesian Distances and polygon perimeters
#
# WITHOUT functions

point_1 = [1.45,2.01]
point_2 = [10.33, 5.22]
point_3 = [-2.45,5.22]
point_4 = [0, 0]

dist_1_2 = math.sqrt((point_2[0] - point_1[0])**2 + (point_2[1] - point_1[1])**2)

dist_2_3 = math.sqrt((point_3[0] - point_2[0])**2 + (point_3[1] - point_2[1])**2)

dist_3_4 = math.sqrt((point_4[0] - point_3[0])**2 + (point_4[1] - point_3[1])**2)

dist_4_1 = math.sqrt((point_1[0] - point_4[0])**2 + (point_1[1] - point_4[1])**2)

# ploygon parimeter

poly_dist = dist_1_2 + dist_2_3 + dist_3_4 + dist_4_1
print(poly_dist)


#%% WITH function for Euclidian Distance

def euclid_dist(point_A, point_B):
    dist = math.sqrt((point_B[0] - point_A[0])**2 + (point_B[1] - point_A[1])**2)
    return dist

poly_dist = euclid_dist(point_1, point_2) + euclid_dist(point_2, point_3) + \
            euclid_dist(point_3, point_4) + euclid_dist(point_4, point_1)

print(poly_dist)