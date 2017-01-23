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
Name:           Week3-3_Numpy.py
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

# Arrays are another data type that we can use within Python
#
# The NUMPY library is one wy to generate and manipulate arrays
#
# Arrays in Numpy can be multi-dimensional
#   1-Dimension = One row of 1 column (like a list)
#   2-Dimensions = multiple rows and columns
#   3+ Dimensions = arrays within arrays OR nested arrays (not that common)
#
# Arrays are useful when you have data that has an specific organization
# Things like:
#   + Time-series data (Time, Value1, Value2...
#   + Geographic data (Lat, Long, Elev, Attributes...)
#   + Items with attributes
#       NAME    att1    att2    att3
#       item1   ...     ...     ...
#       item2   ...     ...     ...
#
#   + Images (raster data) are stored in 2-D array

# The recommened import syntax is:
import numpy as np


# CONSTRUTING ARRAYS
# Arrays are normally contruted as individual rows
# 1-D arrays

one_d = np.array([0,1,2,3,4,5])
print(one_d)

# array attributes

# Length
len(one_d)

# array methods...plus much more
print(one_d.ndim)  # dimensions
print(one_d.size)  # size (for 1-D number of columns)

# 2-D Arrays
# np.array( [ [first row], [second row], [thrid row]...] )

two_d = np.array([[1,2,3,4], [5,6,7,8]])

# or stacked (same thing as above)
two_d = np.array([[1,2,3,4],
                  [5,6,7,8]])

print(two_d.ndim)
print(two_d.shape)

rows = two_d.shape[0]
columns = two_d.shape[1]



#%% Why use arrays????

# easier to store data
# much faster processing times than lists

import timeit

a = np.arange(10000)
%timeit a + 1

b = range(10000)
%timeit [i+1 for i in b]


#%% ARRAY INDEXING / SLICING

# create a 16 element array 1-16 in 4 rows and 4 columns
# np.arange is like the range() func we have used before
# arange(start,end,step) ** end is exclusive (end-1)

# !!! Arrays have single data types (int, float, OR string)
# !!!   np.arange(1.0,17.0) is no tthe same as np.arange(1,17)

import numpy as np

a = np.arange(1.0,17.0)

print(a)

b = a.reshape(4,4)

print(b)

# Array indexing is like lists, except we are referencing the rows and columns
# a[row,column] * remember the first index is 0

# 1-D
print(a[3])

# 2-D
print(b[2,2])
print(b[0,3])

# reasigning single values
b[0,2] = 79.45

# selecting ranges in arrays
# for 1-D, just like lists the format is a[start:end:step]

print(a[0:2])
print(a[::3])

# for 2-D, a[row_start:row_end:row_step, col_start,col_end,col_step]

print(b[1:3,2:3])

# Selecing all the rows in a column, or all columns in a row

print(b[:,2])
print(b[3,:])

#%% Array creation tricks

# arange(start,end,step) ** end is exclusive (end-1)
a = np.arange(1.0,100.0,3)

# linspace(start, end, num-points) ** end is inclusive, without endpint option
b = np.linspace(0, 1, 6)

c = np.linspace(0, 1, 5, endpoint=False)

# Zeros and Ones, arrays of a stated size filled with 0 or 1

zeros = np.zeros((4, 7))
ones = np.ones((3, 3))

# identity arrays (1 on the diagonal, 0 everywhere else) - for linear algebra
eye = np.eye(5)

# random number arrays
#   np.random.rand()
#   np.random.rand(rows,columns)

rand_a = np.random.rand(4)
rand_b = np.random.rand(3,4)

#%% Copying / Views

# Numpy is a little strange...when you create a new variable via indexing
# or slicing you create a "view" of the original array
#   in his example below, a is the original and b is a "View"

a = np.arange(1.0,17.0)
b = a.reshape(4,4)

# views are OK for most things, but for some operations you may get an error:
#    ...this array: it does not own its data
# if this is the case you need to make a COPY of the original array

c = b.resize(6,4)

c = b.copy()
c.resize((6,4))

# you can also copy specific parts of an array
d = b[:2,:2].copy()


#%% Reshapeing

# often we need to transfrom array shapes
# ** the reshaped array must have the same number of elements as the input

a = np.arange(1.0,17.0)
print(a)

b = a.reshape(4,4)
print(b)

#%% Resizing - adding or deleting rows/columns
#
# Copy the original array
# use .resize(rows,columns)

a = np.array([[1,2,3],[4,5,6]])

smaller = a.copy()
smaller.resize(2,2)

bigger = a.copy()
bigger.resize(6,6)

#%% Transposing / Flipping

# Transposing switchs the rows and columns (row 1 > column 1...)

d = c.T

# flipping reverses the order
#   flipud = up/down
#   fliplr = left/right

flip_up = np.flipud(c)

flip_left = np.fliplr(c)

# ** Transposing sometimes falis...
#   The default for a 1-D array is a column vector, sometimes you need a row
#   vector

# this makes a column vector
one_d = np.array([0,1,2,3,4,5])

# transposing should switch it, but it doesn't
one_d_T = one_d.T

# to create a row vector we can use, np.atleast_2d , to force numpy to make a row
one_d_row = np.atleast_2d([0,1,2,3,4,5])

# adding a row to columns
add_row = bigger + one_d_row


#%% MISSING DATA / NaN

# missing data in a numpy array should NOT be stored as zeros, since zeros can
# be a valid value depending on the data
#   think temperature, 0 degrees a temperature not missing data
# in an array we use the convention NaN (not a number)

missing_data= np.array([[1.,2.],
                         [3.,np.nan]])

missing_data_mean = missing_data.mean()
missing_data_nanmean = np.nanmean(missing_data)

#%% ASSIGNING NAN

a = np.random.rand(10)

a[2:4] = np.nan
