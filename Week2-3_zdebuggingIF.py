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
Name:           Week2-3_zdebuggingIF.py
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

import random as rand

# DEBUGGING
#
# Debugging allows us to run our code line by line to find errors
# - In basic code it’s fairly easy to spot errors, but with IFs and loops
#   things can get complicated.

rand_A = rand.randint(0,1000)
rand_B = rand.randint(0,1000)

print("Rand_A = %i and Rand_B = %i" %(rand_A,rand_B))

if rand_A < 300 and rand_B < 300:
    print("A and B are less then 100")
elif rand_A < 300 or rand_B > 300:
    print("A or B is less that 100")
    if rand_A < 300:
        print("A is less than 300")
    else:
        print("B is less than 300")
else:
    print("Neither is less than 100")