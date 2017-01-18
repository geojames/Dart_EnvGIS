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
Name:           Week3-2_zdebuggingFOR.py
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

# Debugging FOR
# basic for loop


my_list = [3,6,12,334,-33,300]

for item in my_list:
    print(item)



#-------
# ex. Two lists, calculate value for first value apply that to another list

slope_percent = [6,20,100]
distance = [10,50,100,500,1000]

# convert slope_percent to gradient and calc drop over given distances

for slp in slope_percent:
    for dist in distance:
        slp_grad = slp / 100
        drop = slp_grad * dist
        print ("A slope of %.3f over %i meters is a %.2f meter drop" %(slp_grad,\
                                                                       dist,drop))

