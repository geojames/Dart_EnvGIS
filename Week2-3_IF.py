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
Name:           Week2-3_IF.py.py
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

# When I use #%% I'm creating a "code cell" which is a part of a script that you
# can run on its own. When you use the "Run current cell" button (right next
# to the big PLAY button, Spyder basically copies the code and runs it in the
# console. It's useful for me during lecture, you may find it useful if you want
# to isolate a specific segment of your code.
#
# ** IF you have cells and just press the big play (Run) button, spyder will
#    ignore the cells and run the script from top to bottom.


#%%

# FORMATTED PRINT STATEMENTS

# https://docs.python.org/3.5/tutorial/inputoutput.html
# https://docs.python.org/3.5/library/stdtypes.html#old-string-formatting

my_int = 3
my_flt = 1004.3
my_str = "hello there"

print(my_str + my_int + my_flt)

# fixed?
print(my_str+str(my_int)+str(my_flt))

# "OLD" style formatted prints
# adding other text...
# use % as a placeholder with a format code
#   list the variables at the end - %(var1,var2,var3,...)
print("%s, my numbers are %i and %0.3f" %(my_str,my_int,my_flt))

# Format codes:
#   i = Signed integer
#   f = floting point decimal (preceeded my a precision value, ie. 0.3f is three decimal places)
#   g = exponetial (1e-4)
#   s = string

# "NEW FORMATTING"
# different placeholders
# curly brackets with sequential numbers for the different variables

# format codes not explicitly needed, it will default to the type of the variable

print('{0} and {1}'.format(my_int,my_flt))

print('{0} and {1:0.3f}'.format(my_int,my_flt))

# be careful the the default formating

my_div = my_flt / my_int

print('{0} and {1:0.3f}, then {2}'.format(my_int, my_flt, my_div))

# ??? add formatting for my_div to show 4 decimal places

print("{0}, my numbers are {1} and {2:0.3g}".format(my_str,my_int,my_flt))

# you don't have to use numbers, you can get fancy...and name your place holders

print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

#%% Basic IF Statement
#
# IF var meets condition:
#    do something...

my_var = -1

if my_var > 0:
    print( "my_var is positive")
    
# the conditions can be simple comparisons
#   or more complex with math or multiple conditions

# essentially IF statements are testing for TRUE or FALSE

#%% IF...ELSE
#
# IF var meets condition:
#    do something...
# ELSE (if not):
#    do something else

my_var = 13458

if my_var % 2 == 0:
    print( "my_var is even")
else:
    print( "my_var is odd")

#%% ELSEIF - adding additional conditions
#
# if var meets condition:
#    do something...
# check another condition:
#    do something...
# if not (ELSE):
#    do something else

# Import the random library to generate random numbers
import random as rand

# Generate a random integer between 1 and 1000
rand_A = rand.randint(0,1000)
rand_B = rand.randint(0,1000)

print( "Rand_A = %i and Rand_B = %i" %(rand_A,rand_B))

if rand_A < rand_B:
    print( "B is greater than A")
elif rand_A > rand_B:
    print( "A is greater than B")
else:
    print( "A = B")

#%% NESTED IF STATEMENTS
#
# You can nest IF statements to check for on condition and then contuinue
# checking other conditions

rand_A = rand.randint(0,1000)
rand_B = rand.randint(0,1000)

print( "Rand_A = %i and Rand_B = %i" %(rand_A,rand_B))

if rand_A != rand_B:
    if abs(rand_A - rand_B) <= 10:
        print( "A is within 10 of B")
    elif 10 < abs(rand_A - rand_B) <= 100:
        print( "A is greater than 10 away, but less than 100")
    elif 100 < abs(rand_A - rand_B) <= 500:
        print( "A is greater than 100 away, but less than 500")
    else:
        print( "A and B are very far apart")
else:
    print( "A = B")

#%% USEING AND and OR in IF STATEMENTS
#
# AND and OR can be used to test multiple conditions in a single IF

rand_A = rand.randint(0,1000)
rand_B = rand.randint(0,1000)

print( "Rand_A = %i and Rand_B = %i" %(rand_A,rand_B))

if rand_A < 300 and rand_B < 300:
    print( "A and B are less then 300")
elif rand_A < 300 or rand_B < 300:
    print( "A or B is less that 300")
    if rand_A < 300:
        print( "A is less than 300")
    else:
        print( "B is less than 300")
else:
    print( "Neither is less than 300")

#%% COMPARING STRINGS
#
# you can compare strings with IF

str_X = "compare"
str_Y = "CoMparE "

if str_X == str_Y:
    print( "X and Y are the same")
elif str_X.lower() == str_Y.lower():
    print( "X and Y are the same letters, but different cases")
else:
    print( "X and Y are not equal")

#%%

# INPUT
#
# input allows you to get input interactivly
# ** All raw inputs are string
# Inputs that need to be numbers need to be converted form string to int or
# float

input_A = input("This is a prompt for an input: ")

input_B = input("Another prompt: ")

print("the first input was " + input_A)
print("the second input was " + input_B)

input_num = float(input("What about a number? "))

print(input_num)

#%%

# ??? Write a short script, where you get two numbers for the user
#       and compare them with an IF statement, print the result!


