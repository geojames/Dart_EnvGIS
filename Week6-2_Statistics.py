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
Name:           Week6-3_Statistics.py
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

# Linear Regression

#%% Scipy stats

from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(1,15,20) + np.random.rand(20)
y = np.linspace(1,15,20) - np.random.rand(20)

slp, intercept, r_val, p_val, std_err = stats.linregress(x,y)

plt.scatter(x,y)
plt.plot(x,(slp*x+intercept))

plt.text(8,4,r'$y = %0.3f x + %0.3f$' %(slp, intercept),fontsize=20)
plt.text(8.5,2,r'$R^2 = %0.4f$' %(r_val**2),fontsize=20)

#%% Numpy

# ploynomial fit
# fit = np.polyfit(x, y, deg)
#   fit[0] * x + fit[1]

fit = np.polyfit(x,y,1)
fit_fn = np.poly1d(fit) 
# fit_fn is now a function which takes in x and returns an estimate for y

plt.plot(x,y, 'yo', x, fit_fn(x), '--k')

# correlation coeff (y vs predicted y)
#   returns 1x2 array [0] = r , [1] = p-value
r = stats.pearsonr(y, fit_fn(x))

# coeff of determination = r^2
r_2 = r[0] ** 2

# for high oreder polynomials the fit array from highest degree to the constant term
# a 2nd order polyfit returns a 1x3 array:
#   fit[0] * x^2 + fit[1] * x + fit[2]
# use polyval(fit,x) to turn the fit into a function

fit2 = np.polyfit(x,y,2)
plt.plot(x,y, 'yo', x, np.polyval(fit2,x), '--b')

r = stats.pearsonr(y, np.polyval(fit2,x))
r_2 = r[0] ** 2


#%% Pandas Regression

dates = pd.date_range('1/1/2016', periods=20)
rows = np.vstack((np.linspace(1,15,20) + np.random.rand(20),\
                np.linspace(1,15,20) - np.random.rand(20),\
                np.linspace(1,15,20) / np.random.rand(20),\
                np.linspace(1,15,20) * np.random.rand(20))).reshape((20,4))
                
data = pd.DataFrame(rows, index=dates, columns=['A', 'B', 'C', 'D'])

ols_model = pd.ols(y = data['A'], x = data['B'])

# typing the var name displays a formatted table of the regression
ols_model

# model variable has lots of dot notation variables
ols_model.resid     # residuals
ols_model.r2        # r^2 value

# quick plot of the fit line

plt.plot(data.B, np.polyval(ols_model.beta,data.B),'r-')
plt.scatter(data.B, data.A)

#%% Multiple regression in Pandas (Panel Regression)

# the Y variable as a separate 
predict = data.B*data.A

model = pd.ols(y=predict, x=data)

model

#%% STATSMODELS

# STATSMODELS is library (pre-installed) for statistical work
#   http://statsmodels.sourceforge.net/

import statsmodels.api as sm

# for two variable regression (x,y) your x data needs to have 2-columns
#   + the extra column is just a ONES array to indicated that the intercept is not zero
#   + don't ask me why, it's just the way STATSMODELS works.
#   + if you just pass the one column each for x and y, you'll get a regression
#           with a intercept of zero
#   + to add the extra column we nee STATSMODEL has a conveient func: add_constant(array)

x = np.linspace(0, 10, 100) - 5 **2
X = sm.add_constant(x)

# OR with column stacking: X = np.column_stack(np.ones(100),(x-5)**2)

Y = x + 0.5 * np.random.normal(size=100)

# linear regression, OLS(y, x)
model = sm.OLS(Y, X)
results = model.fit()
print(results.summary())

results.params
results.rsquared
results.resid

plt.scatter(x,Y)
plt.plot(x,results.fittedvalues,'r-',label='OLS')

# Multiple Linear Regression with Stats Model
#   + X values as columns in an array
xx = np.column_stack((np.ones(100),x, np.cos(x), (x-5)**2))
Y = np.cos(x) + 0.5 * np.random.normal(size=100)

model = sm.OLS(Y, xx)
results = model.fit()
print(results.summary())

plt.scatter(x,Y)
plt.plot(x,results.fittedvalues,'r-',label='OLS')

# tricking STATSMODELS to do regular polynomial regression
# example: 2nd order:  y = Ax**2 + Bx + C
#   Create an array of the terms x**2, x, and a ONES column for the C term
#   run it like a multiple regression
xx = np.column_stack((x**2, x, np.ones(100)))
Y = (x + 0.5 * np.random.normal(size=100)) ** 4

model = sm.OLS(Y, xx)
results = model.fit()
print(results.summary())

plt.scatter(x,Y)
plt.plot(x,results.fittedvalues,'r-',label='OLS')


#%% Non-linear Fitting

# First import the 
from scipy import optimize

# First you need to define a funcion that matches the form of the fit equation
#   you want to use.

def expfit(x, p1, p2):
    return p1 * np.exp(p2*x)
     
# popt, pcov = curve_fit(func, xdata, ydata)
#   popt = optimized parameters matrix (in the order they ar in your func)
#   pcov = covariance stats
#   p0 = (p1,p2,...) - initial guesses at the coeff, optional

popt, pcov = optimize.curve_fit(expfit, x, Y,p0=(3000,-0.2))

plt.plot(x, expfit(x,popt[0],popt[1]),'r-')
plt.scatter(x,Y)
plt.text(-22,350000,r'$%0.4f \times e^{%0.4f x}$' %(popt[0],popt[1]),fontsize=20)

# --------
x = np.linspace(2, 10, 100) * 10 + np.random.normal(size=100)
Y = np.log(x) * 5 + np.random.normal(size=100)

def logfit(x,p1,p2):
    return p1 + p2 * np.log(x)
    
popt, pcov = optimize.curve_fit(logfit, x, Y)

plt.plot(x, logfit(x,popt[0],popt[1]),'r-')
plt.scatter(x,Y)
plt.xlabel("Chipmonks per sq. meter",fontsize=15)
plt.ylabel("Cheetos required to feed them",fontsize=15)
plt.xlim(-0.5,110)
plt.tick_params(labelsize=15)
plt.grid()
plt.text(50,16,r'$%0.4f + %0.4f \times \ln{(x)}$' %(popt[0],popt[1]),fontsize=20)


fig = plt.figure()
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

# log-log plot
ax1.loglog(x, logfit(x,popt[0],popt[1]))
ax1.loglog(x,Y,'bo')
ax1.grid(which='both')
ax1.tick_params(which='both',labelsize=15)

# semilox x plot
#   also works for y-axis
ax2.semilogx(x, logfit(x,popt[0],popt[1]))
ax2.semilogx(x,Y,'bo')
ax2.grid(which='both')
ax2.tick_params(which='both',labelsize=15)

# alternative log setup
ax3.set_xscale("log", nonposx='clip')
# ax3.set_yscale("log", nonposy='clip')

ax3.plot(x, logfit(x,popt[0],popt[1]),'b-')
ax3.scatter(x,Y,s=40, c='m', marker='*')
ax3.grid(which='both')
ax3.tick_params(which='both',labelsize=15)

#%% Other helpful error Stats

# regression residuals
y_predict = np.polyval(fit2,x)
resid = (y_predict - y)
plt.stem(x,resid)

plt.figure()
ax1 = plt.subplot2grid((4,1), (0,0), rowspan=3)
ax2 = plt.subplot2grid((4,1), (3,0))

ax1.scatter(x,y)
ax1.plot(x,np.polyval(fit2,x),'r--')
ax1.set_xlim(np.min(x)-1, np.max(x)+1)
ax1.set_xlabel([""])

ax2.stem(x,resid)
ax2.set_xlim(np.min(x)-1, np.max(x)+1)

# sum of squared error (sse), mean error(me), mean square error(mse), and
#   root mean squared error(rmse)     
sse = np.sum(resid ** 2)
me = np.mean(resid)
mse = np.mean(resid ** 2);
rmse = np.sqrt(np.sum(resid**2)/len(resid))
        