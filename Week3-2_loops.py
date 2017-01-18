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
Name:           Week3-2_loops.py
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

# Line Continuation

'''
Per Python's Formating guidelines PEP-8;
    https://www.python.org/dev/peps/pep-0008
    
-   Limit all lines to a maximum of 79 characters.
-   Limiting the required editor window width makes it possible to have several 
    files open side-by-side, and works well when using code review tools that 
    present the two versions in adjacent columns.
    
    Spyder gives you a vertical bar to tell you when to stop ----------------->
    
    A few characters over is OK, but most code should be kept within the 79
    character limit

'''
# There are two ways to "continue" a long line of code
    
# 1) Simply hit return 

# This...
income = (gross_wages  + taxable_interest + (dividends - qualified_dividends) - ira_deduction - student_loan_interest)

# Becomes this...
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

# 2) use a backslash at the end of a line (older way of doing things)

with open('/path/to/some/file/you/want/to/read') as file_1, open('/path/to/some/file/being/written', 'w') as file_2: file_2.write(file_1.read())

with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
         file_2.write(file_1.read())
         
# Keep indents constant

#%% FOR loops
#
# For loops are used for iteration (looping through) for a finite number
# of iterations
#
# FOR <iterator> in <iterable>:
#    do something for each value in the iterable variable

# **The iterator name should reflect the nature of the list
# basic FOR loop

my_list = [3,6,12,334,-33,300]

for item in my_list:
    print(item)


#%% GENERIC COUNTER with RANGE()
#
# range(start,end,step) creates a temp list of numbers based on the inputs
# i is a traditional counter variable name (also j,k...)

for i in range(10,100,10):
    i_plus20 = i + 20
    print(i_plus20)

#%% Iterating through lists/strings
#
# In Python, FOR loops iterate through each item in the list and the each time
# the iterator gets assigned the next value from the list (basic FOR example above)

strList = ["Hello,", "how", "are", "you?"]

for word in strList:
    print(word)

phrase = "Fun with FOR loops"

for letter in phrase:
    print(letter)

    
# printing whole words, not just letters

word = ""

for letter in phrase:
    if letter != " ":
        word = word + letter
    else:
        print(word)
        word = ""


#%% iterating with indecies
#
# Sometimes , we need to iterate through the items, but sometimes we need to
# loop through something and have access to the index value
# - Possibly to do something on a similar sized list
# - Create a new list with specific index values
#
# use the enumerate(list) function

my_list = [3,6,12,334,-33,300]

for index,item in enumerate(my_list):
    print("For Index %i the value is %i" %(index,item))


#%% ENUMERATE con't

my_list = [3,6,12,334,-33,300]
names = ["Mike", "Stuart", "Alice", "Steve", "Megan", "Kevin"]

for index,item in enumerate(my_list):
    print("For Index %i the value is %i and the name is %s" %(index,item,\
                                                              names[index]))


#%% Nested FOR loops
#
# ex. Two lists, calculate value for first value apply that to another list

slope_percent = [6,20,100]
distance = [10,50,100,500,1000]

# convert slope_percent to gradient and calc drop over given distances

for slp in slope_percent:
    for dist in distance:
        slp_grad = slp / 100.0
        drop = slp_grad * dist
        print("A slope of %.3f over %i meters is a %.1f meter drop" %(slp_grad,\
                                                                      dist,drop))


#%% WHILE Loop
#
# Use when the iteration length is indeterminate or could change based on
# conditions.
# - Best for waiting for a condition to be met
# - Often used with user input, allows for infinite looping until the user
#       input a acceptable value
# - File reading – data files can vary in length
#
# ***WARNING***
#   While loops are prone to being infinite, be careful...

import random as rand

i = 0
rand_A = rand.randint(0,1000)
rand_B = rand.randint(0,1000)

while rand_A != rand_B:
    rand_A = rand.randint(0,1000)
    rand_B = rand.randint(0,1000)
    i += 1

# print the number of iterations it took for A and B to be equal
print(i)

#%% User input

# blank string variable
user_txt = ""

# wait for a specific answer, if the input is not 42 continue to loop until it is
while user_txt != "42":
    user_txt = input("What is the answer to life, the universe, and everything? ")


#%% Continuous inputs with WHILE

lines = list()
first_line = input("Enter a value for the first number: ")
lines.append(float(first_line))

# condensed version
# lines.append(float(input("Enter a value for the first line: ")))

testAnswer = input('Press y if you want to enter more numbers: ')

while testAnswer == 'y':
    line = input('Next line (enter n to stop): ')
    if line != "n":
        lines.append(float(line))
    else:
        testAnswer = 'n'

for line in lines:
    print(line)

#%% BREAKS
#
# Breaks allow us to get out of a loop (mid-loop if nessesary)
# - A break will only exit out one level in nested loops
#
# In FOR/WHILE loops breaks are usually paired with and IF statement to activate the break

# User input for type of calculation with error checking, only 1 and 2 are
# allowed. Continue in a loop until 1 or 2 is entered.


while True:
    print("What would you like to calculate?")
    print("Enter 1 for daily average discharge")
    print("Enter 2 for daily maximum discharge")
    option = input(" Option = ")
    if option.isdigit():
        if int(option) == 1 or int(option) == 2:
            print("OK, you chose option %s" %option)
            break
        else:
            print("Try again...\n")
    else:
        print("Try again...\n")


#%% LIST Comprehensions
#
# Small, automatic FOR loops for lists
# 
# NOTE: I dont usually use these, but for some of you they may come in handy

my_list = [10,50,100,500,1000]

# list_math = list()
# for num in my_list:
#    list_math.append(num**2)

# with comprehensions we can shorten this to one line
list_math = [num**2 for num in my_list]
print(list_math)

