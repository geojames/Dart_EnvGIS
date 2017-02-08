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
Name:           Week7-1_StatisticsTwo.py
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

# Distribution Fitting

import os
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


B = np.random.normal(50,12,300)
plt.hist(B)

# percentiles 

B_p16 = np.percentile(B,16)
B_p50 = np.percentile(B,50)
B_p85 = np.percentile(B,85)

# probability density functions
B.sort()
plt.hist(B, normed='true')
plt.plot(B,stats.norm.pdf(B,np.mean(B),np.std(B)),'r-',linewidth=2.0)

# cumulative density functions
plt.plot(B,stats.norm.cdf(B,np.mean(B),np.std(B)))


#%%

# Hypothesis Testing

A = np.random.normal(50,12,300)
B = np.random.normal(55,15,300)

plt.hist(A,alpha=0.75)
plt.hist(B,alpha=0.75)

A.sort()
B.sort()

plt.plot(A,stats.norm.pdf(A,np.mean(A),np.std(A)),'b-',linewidth=2.0)
plt.plot(B,stats.norm.pdf(B,np.mean(B),np.std(B)),'r-',linewidth=2.0)

# T-Test of independant samples
# If the p-value is smaller than the threshold, e.g. 1%, 5% or 10%, 
#   then we reject the null hypothesis of equal means

t_stat,p_val = stats.ttest_ind(A,B)

#%%

# Interolation

from scipy import interpolate as interp

# linear interpoalation

x = np.linspace(-5,10,10)
y = np.sin(x)*np.random.rand(len(x))

# create interpolation functions
# linear: interp1d(x,y)
# cubic spline: interp1d(x, y, kind='cubic')
#   other kinds: quadratic, nearest

f = interp.interp1d(x,y)
f2 = interp.interp1d(x, y, kind='cubic')
f3 = interp.interp1d(x, y, kind='nearest')
f4 = interp.interp1d(x, y, kind='quadratic')

x_ext = np.linspace(-5,10,100)

plt.scatter(x,y)
plt.plot(x_ext,f(x_ext),'-b', label="linear")
plt.plot(x_ext,f2(x_ext),'-r', label="cubic")
plt.plot(x_ext,f3(x_ext),'g--', label="nearest")
plt.plot(x_ext,f4(x_ext),'m--', label="quadratic")
plt.legend()

# single value
f(-1)

# 2-d interpolation

#%% 2D Interp using radial basis function

def f(x,y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

# real function (from Matplotlib adv lecture)
n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
xg,yg = np.meshgrid(x, y)

z = f(xg,yg)

# generate sample points 
sample = np.random.randint(-3,3,(150,2)) + +np.random.normal(0,1,(150,2))

zs = f(sample[:,0],sample[:,1])

# create a mesh to interoplate on to
xx, yy = np.meshgrid(np.linspace(sample[:,0].min(),sample[:,0].max(),80),\
            np.linspace(sample[:,1].min(),sample[:,1].max(),80))
            
# generate a radial basis fuction
# default multiquadratic
rbf1 = interp.Rbf(sample[:,0],sample[:,1],zs, epsilon=2)
zz1 = rbf1(xx,yy)

# thin plate spline
rbf2 = interp.Rbf(sample[:,0],sample[:,1],zs, function='thin_plate')
zz2 = rbf2(xx,yy)

# linear
rbf3 = interp.Rbf(sample[:,0],sample[:,1],zs, function='linear')
zz3 = rbf3(xx,yy)

# inverse distance weighted
rbf4 = interp.Rbf(sample[:,0],sample[:,1],zs, function='inverse')
zz4 = rbf3(xx,yy)


plt.subplot(2,3,1)
plt.pcolor(xg,yg,z,cmap='hot')
plt.title("ORIGINAL")
plt.subplot(2,3,2)
plt.pcolor(xx, yy, zz1, cmap='hot')
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.title("Multi-Quad")
plt.subplot(2,3,3)
plt.pcolor(xx, yy, zz2, cmap='hot')
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.title("Thin plate")
plt.subplot(2,3,4)
plt.scatter(sample[:,0],sample[:,1],30,c=zs, cmap='hot')
plt.title("Scatter")
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.subplot(2,3,5)
plt.pcolor(xx, yy, zz3, cmap='hot')
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.title("Linear")
plt.subplot(2,3,6)
plt.pcolor(xx, yy, zz4, cmap='hot')
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.title("IDW")

#%% 2D Interp w/ GridData

grid_z0 = interp.griddata(sample, zs, (xx, yy), method='nearest', fill_value=np.nan, rescale=False)
grid_z1 = interp.griddata(sample, zs, (xx, yy), method='linear', fill_value=np.nan, rescale=False)
grid_z2 = interp.griddata(sample, zs, (xx, yy), method='cubic', fill_value=np.nan, rescale=False)

plt.subplot(2,3,1)
plt.pcolor(xg,yg,z,cmap='hot')
plt.title("ORIGINAL")
plt.subplot(2,3,2)
plt.pcolor(xx, yy, grid_z0, cmap='hot')
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.title("nearest")
plt.subplot(2,3,3)
plt.imshow(grid_z1, cmap='hot',extent=(-3,3,-3,3), interpolation='none',origin='lower')
plt.title("Linear")
plt.subplot(2,3,4)
plt.scatter(sample[:,0],sample[:,1],30,c=zs, cmap='hot')
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.title("Scatter")
plt.subplot(2,3,5)
plt.imshow(grid_z2, cmap='hot',extent=(-3,3,-3,3), interpolation='none',origin='lower')
plt.title("cubic")

#%% Moving averages

#os.chdir("C:/Users/f0022gc/Dropbox/Teaching/2015/Code/data")
os.chdir("C:/Users/James/Dropbox/Teaching/2015/Code/data")

olym_WX = pd.read_csv('Olympia_Dec2015.csv',parse_dates=[['Date', 'Time']])
olym_WX = olym_WX.set_index(['Date_Time'])

plt.plot(olym_WX.index,olym_WX.DryBulbCelsius)

olym_DailyMean = olym_WX.DryBulbCelsius.resample("d", how='mean')
olym_DailyMax = olym_WX.DryBulbCelsius.resample("d", how='max')
olym_DailyMin = olym_WX.DryBulbCelsius.resample("d", how='min')
olym_DailyRange = olym_DailyMax - olym_DailyMin

plt.bar(olym_DailyRange.index,olym_DailyRange.values,bottom=olym_DailyMin.values)

plt.fill_between(olym_DailyMin.index,olym_DailyMin.values, olym_DailyMax.values)

olym_4HMean = pd.rolling_mean(olym_WX.DryBulbCelsius, 4)
olym_12HMean = pd.rolling_mean(olym_WX.DryBulbCelsius, 12)
olym_24HMean = pd.rolling_mean(olym_WX.DryBulbCelsius, 24)
olym_72HMean = pd.rolling_mean(olym_WX.DryBulbCelsius, 72)

plt.plot(olym_4HMean)
plt.plot(olym_12HMean)
plt.plot(olym_24HMean)
plt.plot(olym_72HMean)

#%%

# Color Ramp Stretching
# http://matplotlib.org/devdocs/users/colormapnorms.html