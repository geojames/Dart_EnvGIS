# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Name:         Week1-2_Lecture.py
# Purpose:      Example and Notes for Week 1 Lecture
#
# Compatibility: Python 3.5
#
# Author:       James Dietrich, Dartmouth College
#               james.t.dietrich@dartmouth.edu
# Created:      Wed Jan 06 09:18:15 2016
# Copyright:    (c) James Dietrich 2015
# Licence:      MIT
#
#------------------------------------------------------------------------------

#%% ------
# Variable Types

# NUMBERS
# Integers - whole numbers (no decimals)
x = 1
y = 10

z = x - y
z = x / y

# Float - Floating point decimal numbers

a = 1.0
b = 3.4445

c = b - a
c = a / b

#%% -----
# STRING (sequence of characters)

my_text = "This is a test string."

# Numbers as strings
number = "42"
numb_str = str(42)

# back to a number
numb_int - int(numb_str)
numb_float = float(numb_str)

# to add single-quotes and apostrophes the outter quotes must be double "__"
quotes = "adding 'quotes' or apostrophe's in a string"

# double-quotes can be added using the "escape" charater backslash -- this is 
# important because a single backslash will never work for you!

double_quotes = "this shows how \"double quotes\" are inserted"

# since the backslash is the escape charater, double backslash add the slash
# useful for file paths
double_quotes = "c:\\windows\\users\\James\\Desktop"

# in Python file paths can also be defined with forward slashes
File_paths = "C:/Windows/Users/James"

# Sting methods
my_text.upper()

# string indexing
# | P | Y | T | H | O | N |
#   0   1   2   3   4   5
text = "python"
print(text[0])
print(text[6])

print(test[1:5])  # print characters 1-4, 5 will not print.

#%%------
# BOOLEAN Values - True and False
ducks = True
flying_pigs = False

# Boolean through comparison
# >, <, >=, <=, !=, ==

ans = 3 > 4
ans = 5 != 3.3
ans = 4 == 3


#%%***************
# NAMING VARIABLES

# i.	Readable names or common abbreviations

number = 45
numb = 45
temperature = 0
temp = 0

# ii.	Single letters (upper or lower) – never use low el, cap o, cap i
x = 5
y = 3

# iii.	lowercase, lower_with_underscores, UPPER, UPPER_UNDER
birds = ["robin", "jay", "titmouse"]
birds_with_crests = ["cardinal", "titmouse"]

# Spyder Excludes UPPERCASE variables from the variable list on the right  --> test it
LAKES = ("michigan", "erie")
NUM_LAKES = 4

# iv.	CapWords (camel case)
TempCel = 40
TempFer = TempCel * 1.8 + 32

# v.	mixedCase (small firstword, capital others)
riverFlow = [22,24,56,78,55,34]
pressureKpa = [103.4,104.3,104.6]

# vi. Can’t start with numbers, some variable names are “reserved” for python

3rivers = 3
del = 45
from = "to this"

#%% *******************
# MATH OPERATIONS

# Common:
#   +   addition
#   -   subtraction
#   *   multiplication
#   /   division (true float division)
#   **  exponent

#   %   modulo (remainder after division)
#   //  floor division (whole number without remainder)

# Order of Operations –
# PEMDAS : Parentheses, Exponents, Multi/Divide, Add/Subtract

# Adding parenthesis usually increases readability
# EX: eucilian distance between two points

import math
# use math.sqrt(...) to find the square root of a number or function

x1 = 3.5
y1 = 4.3

x2 = 9.0
y2 = 0.2

# ??? type out the equation for the eqlidean distance between the two points

dist = math.sqrt((x2-x1)**2+(y2-y1)**2)

#%% ********************
# COMMENTING
#
# Comments in your code are key:
#  i.	For you to remember what’s going on, if nothing else
#  ii.	Also for others…
#  iii.	“Always code and comment as if your life depends on someone else
#          understanding your code.”

#  In Python the convention is to use “block comments” at the beginning
#  of a “code block”
# EXAMPLE:
#----

# User input for exact field of view angles (FOVs). Error check that the inputs
# are float values. Continue in a loop until all values are float.
# (If unknown, scour the web the answer is out there...)
while True:
    print("Enter the field of view for the lens (take from image dimensions)-")
    xAngle = raw_input(" X (horz) angle: ")
    yAngle = raw_input(" Y (vert) angle: ")
    if isFloat(xAngle) and isFloat(yAngle):
        xAngle = float(xAngle)
        yAngle = float(yAngle)
        print("\n")
        break
    else:
        print("***X and Y dimensions need to be numbers, please try again\n")

#----
# Block comments are better than “inline” comments
# Inline EXAMPLE:
#----

while True:     # While values are not valid
    print("Enter the field of view for the lens (take from image dimensions)-") # Print instructions
    xAngle = raw_input(" X (horz) angle: ")     # get user input for x angle
    yAngle = raw_input(" Y (vert) angle: ")     # get user input for y angle
    if isFloat(xAngle) and isFloat(yAngle):     # If the values pass FLoat test:
        xAngle = float(xAngle)                  # make xAngle float
        yAngle = float(yAngle)                  # make yAngle float
        print("\n")                              # print new line to console
        break                                   # break While loop
    else:           # if values do not meet float condition
        print("***X and Y dimensions need to be numbers, please try again\n")  #Print error and repeat

