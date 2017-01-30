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
Name:           Week4-2_Matplotlib_Intro.py
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

# Inline in Ipython or in a separate QT window
%matplotlib inline  # inside the console, fine for quick plots
%matplotlib qt5      # in separate window, better for most applications

import numpy as np

# two different ways to import the primary 2D plot library , PyPlot
from matplotlib import pyplot as plt
    # OR
import matplotlib.pyplot as plt


# Figures, Axes, and Subplots
#
# Figure = Blank container for plots
# Subplots = a way to orgainize multiple inside a figure
# Axes = Axes for individual plot(s)

# there are attributes you can set/change associated with each level

# for basic plots like:

x = np.linspace(-5,5,300)
ysin = np.sin(x)
ycos = np.cos(x)

plt.plot(x,ysin)

# a figure and axis are created automatically
# matplotlib allows you to add to, or change chage attributes for whichever
#   figure you have just created

plt.plot(x,ycos)
plt.scatter(x+1,ysin)

# to create multiple graphs in separate figure windows you need to create new
#   figures

fig1 = plt.figure()
plt.plot(x,ysin)

fig2 = plt.figure()
plt.plot(x,ycos)

#%%
# Basic Line Properties & Stypes
#   http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot

x2 = np.arange(1.0,100.0,5)
y = x2/2.0
y2 = np.log(x2 ** 2) * 5

# Line Styles
#   '-'  or 'solid'     solid line
#   '--' or 'dashed'    dashed line
#   '-.' or 'dashdot'   dash-dotted line
#   ':'  or 'dotted'    dotted line

# Colors
# http://matplotlib.org/examples/color/named_colors.html

# Some color shortcuts:
#   k = black   w = white   b = blue
#   g = green   r = red     m = magenta
#   y = yellow  c = cyan


# explicit definition
plt.plot(x2,y, color="blue", linestyle="-")

# shortcuts
plt.plot(x2,y2,'r--')  # dashed red line
plt.plot(x2,y2,'r-')   # solid red line

# markers
# http://matplotlib.org/api/markers_api.html#module-matplotlib.markers

#   "." = point     "o" = circle    "*" = star
#   "+" = plus      "x" = x         "^" = triangle_up

plt.plot(x2,y, color="blue", linestyle="-", marker='o')

# shortcuts: red, dashed, with X markers
plt.plot(x2,y2,'r--x')

# line witdh
plt.plot(x2,y, color="blue", linestyle="-", marker='o',linewidth=2.0)

# labels for the legend (always a good idea...)
plt.plot(x2,y, color="blue", linestyle="-", marker='o', label="x/2")
plt.plot(x2,y2,'r--x',label='log(x^2)*5')

plt.legend(loc='upper left')

# Multiple lines/formats in one call
#   plt.plot (x1, y1, options..., x2, y2, options...)

plt.plot(x2,y,'b-o',x2,y2,'r--')

#%% Basic Axes Settings

plt.plot(x2,y, color="blue", linestyle="-", marker='o', label="x/2")
plt.plot(x2,y2,'r--x',label='log(x^2)*5')

# X/Y limits (min, max)
plt.xlim(-10,150)
plt.ylim(-20,70)

# X/Y Ticks (array of tick locations, <array of labels>, <rotation=angle>)
xticks = np.arange(-10,150,10)
yticks = np.arange(-10, 70, 13)

plt.xticks(xticks,fontsize=14)
plt.yticks(yticks)

# X/Y labels
plt.xlabel("This is the X-axis")
plt.ylabel("This is the Y-axis")

# Legend
#   http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.legend
plt.legend(loc='upper left')

plt.title('WOOHOO!! a graph')

#%% SUBPLOTS

# Subplots allow you to create multiple tiled plots in one figure

#   plt.subplot(<num of rows>, <num of columns>, <plot number>)
#
#   for 3 plots in a row:
#   ----------------------------------
#   |          |          |          |
#   |          |          |          |
#   | (1,3,1)  |  (1,3,2) | (1,3,3)  |
#   |          |          |          |
#   |          |          |          |
#   ----------------------------------

#   4 plots (2x2)
#   -----------------------
#   |          |          |
#   | (2,2,1)  | (2,2,2)  |
#   |          |          |
#   -----------------------
#   |          |          |
#   | (2,2,3)  | (2,2,4)  |
#   |          |          |
#   -----------------------

plt.subplot(3,1,1)
plt.plot(x, ysin)
plt.ylim(-1.1,1.1)

plt.subplot(3,1,2)
plt.plot(x, ycos)
plt.ylim(-1.1,1.1)

plt.subplot(3,1,3)
plt.scatter(x2,y2)
plt.xlim(0,120)
plt.ylim(0,50)
plt.grid()

# you can do things in serial steps (above) or you can setup your subplot so
#   that you have access to the individual axes

# with individual axes defined, you can plot and access the attributes through
#   dot notation for each axes
#       ** the attributes are a little different, most start with ax1.set_...
#   ax1.plot(x,ysin)
#
#   If you make a mistake you can use the clear command, ax3.clear()

Z = np.random.rand(20,20)

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

ax1.plot(x2,y2,'k')

ax2.pcolor(Z)

ax3.scatter(x2,y)

ax4.plot(x,ysin,'r',x,ycos,'b')

# You can also create subplot in interesting arragnements with the
# subplot2grid function
#   plt.subplot2grid((rows,cols), (row index,column index))
#       - you can aslo have the axes "span" multiple rows or columns

ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
ax2 = plt.subplot2grid((3,3), (1,0), colspan=2)
ax3 = plt.subplot2grid((3,3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3,3), (2, 0))
ax5 = plt.subplot2grid((3,3), (2, 1))

ax1.plot(x,ysin)
ax1.plot(x,ycos,'r.')
ax1.set_ylim(-1.1,1.1)

ax2.plot(x2,y2)

ax3.barh(x2,y,align='center',height=0.9)

ax4.plot(x,ysin, 'b--',linewidth=2)
ax4.fill_between(x,0,ysin,ysin<=0,color='blue',alpha=0.75)
ax4.fill_between(x,0,ysin,ysin>0,color='red',alpha=0.75)
ax4.set_ylim(-1.1,1.1)
ax4.set_xlim(x.min(),x.max())

ax5.pcolor(Z,cmap='spectral')

#%% Real Data

import os
import pandas as pd
import matplotlib.dates as dates

# Montshire Museum Weather Data from WeatherUnderground (Station ID: KVTNORWI2)
#   downloaded via http://oco-carbon.com/weather/access.html

# WINDOWS
os.chdir("C:/Users/James//Documents/GitHub/Dart_EnvGIS/Data/")

# MAC
os.chdir("/Users/ryanmckeon/GitHub/Dart_EnvGIS/Data/")

infile = "KVTNORWI2_2016-12-1_2017-01-26.csv"

Mont_wx = pd.read_csv(infile,parse_dates=[0],keep_date_col=True)

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ax1.plot(Mont_wx.Time,Mont_wx.TemperatureC,'b-')

ax1.xaxis.set_major_formatter(dates.DateFormatter('%m-%d-%H:%M'))
plt.setp(ax1.get_xticklabels(), rotation=45, fontsize=10, ha='right')

ax1.set_xlabel("Date")
ax1.set_ylabel("Temp. (°C)")
ax1.set_title("Montshire Temp: Dec 1,2016 - Jan 26, 2017")
fig.tight_layout()


# --

fig2 = plt.figure()
ax1 = fig2.add_subplot(1,1,1)

ax1.plot(Mont_wx.Time,Mont_wx.PressurePa,'b-',)

ax1.xaxis.set_major_formatter(dates.DateFormatter('%m-%d-%H:%M'))
plt.setp(ax1.get_xticklabels(), rotation=45, fontsize=10, ha='right')

ax1.set_xlabel("Date")
ax1.set_ylabel("Pressure (Pa)")

ax2 = ax1.twinx()
ax2.plot(Mont_wx.Time,Mont_wx.WindSpeedKMH,'ro')
ax2.set_ylim(0,50)
ax2.set_ylabel("WindSpeed (KMH)")

ax1.set_title("Montshire Pressure vs. Windspeed:\nDec 1,2016 - Jan 26, 2017")
