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
Name:           Week4-1_Numpy2.py
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


import numpy as np
import timeit

#%% ARRAY MATH
#
# Doing math on entire arrays is much faster than using lists and FOR loops

a = np.arange(10000)
%timeit a + 1

b = list(range(10000))
%timeit [i+1 for i in b]


#%% Element wise operations

import numpy as np

array = np.array([[1.,2.,3.,4.],
                  [5.,6.,7.,8.]])


# math operations are "element-wise", any math operation will be applied to
# each element of the array

plus_1 = array + 1

array_squ = array ** 2

array_func = 10 ** (array/2)

#%% Array to Array Math

# for equal sized arrays, the math is done on matching elements
a = np.array([[1.,2.,3.,4.],
             [5.,6.,7.,8.]])

b = a * 10

c = a + b

# Can also work on array with different dimensions (as long as one dimension is
#   is same, same number of row or columns) - sometimes called broadcasting
# The smaller array will be "broadcast" to the other rows/columns

a = np.array([[1.,2.,3.,4.],
             [5.,6.,7.,8.]])

b = np.array([10,11,12,13])

c = np.array([[1.],
             [20.]])

col_wise = a + b

row_wise = a + c

# combining operations

array = a + c**2

#%% ARRAY CONCATENATION

# Combining arrays is easy, but beware of the direction and size of your inputs
# the number of elements that you sticking on must be the same dimensions

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

# to concat B onto A (rows)
np.concatenate((a, b), axis=0)

# to add B as a column you need to transpose it
np.concatenate((a, b.T), axis=1)

# vstack and hstack
v_stack = np.vstack((a,b))

h_stack = np.hstack((a,b.T))

np.row_stack((a,b))
np.column_stack((a,b.T))

#%% ARRAY REDUCTION

# most array reductions are methods availible to an existing array
# other reductions are numpy functions

# SUMS

a = np.array([[1.,2.],
             [3.,4.]])

# sum of all elements
a_sum = a.sum()

# sums of rows (axis=0) or columns (axis=1)
# output is an array
#        ax1
#   a   1   2
#   x   3   4
#   0

a_sum_rows = a.sum(axis=0)
a_sum_cols = a.sum(axis=1)

# MIN / MAX
# can also do by axis (like sums)

a_max = a.max()     # a_row_max = a.max(axis=0)
a_min = a.min()

# BASIC STATS
# !! for data with nan values use the nan stats functions:
#       np.nanmean(array) or np.nanmean(a, axis=)...

a_xbar = a.mean()           # a_col_mean = a.mean(axis=1)

a_median = np.median(a)     # a_col_median = np.median(a, axis=1)

a_std = a.std()             # a_row_std = a.mean(axis=0)

#%% UNIQUE VALUES

years = np.random.randint(1950,2016,100)

unique_list = np.unique(years)

uniq, counts = np.unique(years, return_counts=True)
u_counts = np.vstack((uniq, counts)).T

#%% SORTING

# sorting in basic numby arrays is tricky...the default sort method sorts
# everything based on the axis you choose (0 or 1)

array = np.arange(1,9)
rand_data = np.random.randint(1,100,(8))
a_data = np.vstack((array,rand_data)).T

a_srt = np.sort(a_data,axis = 0)    # independantly sorts all columns low-high

a_srtR = np.sort(a_data,axis = 1)    # independantly sorts all rows low-high

# usually you want to sort a matrix by a specific row or column, so that your
# data stays together. For this we use a fancy indexing method with np.argsort

np.random.shuffle(a_data)

a_data[np.argsort(a_data[:,0])]

a_data[np.argsort(a_data[:,1])]

sort = a_data[a_data[:,1].argsort()]

#%% MASKING or BOOLEAN INDEXING / EXTRACTION

# you can "select" elements of your array based on a boolean test
#

a = np.random.random_integers(-20, 20, (10,10))

mask = (a <= 0)

# Extracted elements will be in a 1-D array
a_extract = a[mask]

# inverse masking
a_inverse = a[not mask]

# short cut, ~ = not
a_inverse = a[~mask]

# direct masking, putting the boolean inside the index
a_dir_mask = a[a >= 0]

# masks can also be used to select elements in other arrays of the same size

b = np.arange(0,10)

b_mask = b[mask]

# doing math with masks (reasigning)

a[mask] = a[mask] * 100

#%% ASSIGNING NAN

a = np.random.rand(10)

mask = (a >= 0.5)

a[mask] = np.nan

#%% STRUCTURED ARRAYS

# arrays that allow you to manipulate the data based on named fields
# also allow for different data types to be stored in the same array
#   - Pandas Data Frame to do mostly same thing
#   ** you're better off using Pandas for this type of data **

# DTYPES
#   + Common dtypes:
#       - 'b'	boolean
#       - 'i'	(signed) integer
#       - 'f'	floating-point
#       - 'S', 'a'	(byte-)string
#       - 'O'	(Python) objects (i.e. datatime objects)

# Contructing structured arrays
#
a = np.array([(1.0, 2), (3.0, 4)], dtype=[('x', float), ('y', int)])


'''

Lab 3 Grading Rubric

• Does the program calculate the distance correctly (i.e. does it agree with 
  the website provided)? 0-5 pts.
                                                     
• Does the program get user inputs from the console and successfully screen 
  them for errors? 0-5 pts.
  
• Does the program print the required outputs to the console and are they 
  explained in a manner that the user knows what they are getting? 0-5 pts.
  
• Do the comments embedded in the code sufficiently explain the work flow and 
  the commands that are being executed (i.e. can I understand what your code is 
  doing without having to interpret commands from their actual syntax)? 0-5 pts.
                                                            
• Extra Credit parts – Same criteria apply, 3 pts. available

