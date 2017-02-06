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
Name:           Week6-1_Pandas.py
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

# Pandas provides a set of labeled array data structures
# Similar to what you're used to in Excel
#   + 1-D "Series"
#   + 2-D "Data Frames"


# Import Pandas
import pandas as pd

# You also need Numpy
import numpy as np

# and Matplotlib, if you want to plot data
import matplotlib.pyplot as plt

#%% Creating Pandas data

# chances are you'll be importing data into Pandas with read_csv, which we'll
#   get to...but you'll also need to create Pandas data from scratch too

# Pandas uses two data structures:
#   Series = 1-D data (single column)
#   Data Frame = 2-D data (multiple columns)

# Terms:
#   + Column = actual data
#   + Index Column =  first column, defaults to numbers, but also you can 
#           also name rows in the index column or use dates as the index column
#           * Yes, it is confusing, since data frames still have indecies like
#             arrays...
#
# The general structure of a data frame is:
#
# Index	COL1	COL2	COL3	...
# 1		data	data	data
# 2		data	data	data
# 3		data	data	data
# 4		data	data	data
# ...

# of for real data would look something like this:
    
# Index	temp   pres	wind    wind_dir	...
# 1		26.2   1012.3	0		nan
# 2		27.0   1011.1	5		"w"	
# 3		27.8   1011.5	8		"nw"
# 4		24.3   1011.3	5		"w"	
# ...

# 1-D series data are easy...
s = pd.Series([1,3,5,np.nan,6,8])

# 2-D data can be created in a couple different ways

# 1: typing in matrix vaules
df = pd.DataFrame([[1,2,3,4,5], [6,7,8,9,10]],columns=['A','B','C','D','E'])

# 2: from an exisitng Numpy Array
array = np.array([[1,2,3,4,5], [6,7,8,9,10]])
df2 = pd.DataFrame(array)

# 3: numpy array with column names
array = np.arange(1.,17.).reshape((4,4))
df3 = pd.DataFrame(array, columns=['A','B','C','D'])

# adding columns
# df['new column name'] = data to add...

colors = pd.Series(['blue','green','red','yellow'])

df3['color'] = colors
   
# directly...
df3['food'] = np.array(['fish','lettcue','apple','banana'])

#%% Accessing index and column name lists

df.index
df.columns
df.values
df.dtypes
df.describe()

#%% Accessng/adding/deleting column data

# access the column by name: string OR by dot notation

df3['A']

df3.A

# adding data
 
df3['color'] = pd.Series(['blue','green','red','yellow'])

df3['random'] = np.random.rand(4,1)

# new columns by math

df3['AxRand'] = df3.A * df3.random

# boolean tests as columns

df3['Blue_TF'] = df3.color == 'blue'

# adding one value to all rows (propogated value)

df3['ones'] = 'one'

# deleting columns

del df3['random']

# extracting values and deleting (pop out)
rand_vals = df3.pop('AxRand')


# Inserting new columns
#   insert(position, col_name, values)

df3.insert(0,'AxR',rand_vals)

#%% Date ranges

# often your data will need dates. Pandas has some nifty short cuts for adding
# dates to your data frames

# Start and end dates with frequency
#   pd.date_range(start, end, freq = 'D')

pd.date_range('1/1/2016','12/31/2018')


# Start, frequency and number or periods
#   pd.date_range(start, periods=10, freq='D')

# Frequency Codes
#   'A' = year end - 'AS' = year start
#   'M' = month end - 'MS' = month start
#   'W' = week
#   'D' = days, default
#   'H' = hours
#   'min' = minutes
#   's' = seconds
#
#   '5H' = 5 hours, '30s' = 30 seconds, '7D' = 7 days

pd.date_range('1/1/2016',periods=10, freq='D')

pd.date_range('1/1/2016',periods=10, freq='min')

# adding time (24-hour format)

pd.date_range('1/1/2016 07:30:00',periods=10, freq='30d')

#%% Data Frame Indexing

dates = pd.date_range('1/1/2016', periods=8)

df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])

# Getting Columns
df.A
df['B']

# Rows, all columns
# by classic index
df[0:4]

# by named index range
df['2016-01-02':'2016-01-04']

# using the location (loc) function
#   dates index, row 0
df.loc[dates[0]]

#   row and column
df.loc[2:4,['A','B']]

#   index and columns
df.loc[dates[2],'A']    # or is you have a generic index: df.loc[index[2],'A']

# Pure index locations (iloc) function
# rows and columns, like arrays
df.iloc[3:5,0:2]

#%% Data Frame Math

# Math on an entire Data Frame
df2 = df * 3

# In place replacement (not recommended, but good for recalculating and overwriting)
df.B = df.B * 2

# better to create a new column
df['Btimes2'] = df.B * 2

# math between columns
df['convert'] = ((df.A * 9/5) + 32) - df.C

# math for specific indecies
df['indexMath'] = df.D[2:5] ** 2

# math with boolean masks
#   only apply the equation to positive vaules in A
df['convertPos'] = ((df.A[df.A >=0] * 9/5) + 32) - df.C[df.A >=0]

#   Apply a different equation to the negative values
df.convertPos[df.A < 0] = ((df.A[df.A < 0] * 9/5) + 32) + df.D[df.A < 0]

#%% Reduction

dates = pd.date_range('1/1/2016', periods=8)
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])

# Basic stats (default is columns, and to skip NaN values)
#       for row stats add (axis=0)
df.mean()
df.std()
df.median()

# Getting statistics for a specific column
df.A.mean()

# Sums (again by column)
df.sum()
df.B.sum()

#%% Combining / Adding Values

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                    index=[4, 5, 6, 7])

series = pd.Series(['X10', 'X11', 'X12', 'X13'], name='X')

result = pd.concat([df1, df2])
result2 = pd.concat([df1, df2], axis = 1)

result = df1.append(df2)

result = pd.concat([df1,series],axis=1)

# combining data with matching indicies
dates = pd.date_range('1/1/2016', periods=8)
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])

dates = pd.date_range('1/4/2016', periods=8)
df2 = pd.DataFrame(np.random.randn(8, 2), index=dates, columns=['E', 'F'])

df3 = pd.concat([df, df2], axis=1)

#%% Converting Pandas to Numpy

# single column
np_from_pd = pd.np.array(df3.A)

# whole thing
np_from_pd = pd.np.array(df3)

# using numpy santax
array = np.array(df3.values)

# Monster statments with multiple instructions
np_with_reshape = pd.np.array(df3.A).reshape((2,2))

