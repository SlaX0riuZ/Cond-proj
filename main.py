# Comparison Operators Task
# Programmed by SlaX0riuZ
# Date // 10-29-2024
# Version Alpha v0.0.1

# Program created for Intro to Python class

import math

# get a single string of input from user
n_c = input("Enter two numbers to compare, separated by a space: ")
print("--------------------")

n_list = n_c.split() # turns the string into the two numbers

# n_list[0] is the user's first number
# n_list[1] is the user's second number
try:
    n1 = float(n_list[0]) # convert to float for easy manipulation
    n2 = float(n_list[1])
    if len(n_list) > 2:
        raise IndexError # user must have inputted > 2 numbers
except ValueError:
    print("Please type in numbers, not text.")
except IndexError:
    print("Please input only two numbers.")
else: # run the rest of the program
    dn1 = str(n1) # make concatenation easier
    dn2 = str(n2)
    if n1 < n2:
        print(dn1 + " is less than " + dn2)
    elif n1 == n2:
        print(dn1 + " is equal to " + dn2)
    elif n1 > n2:
        print(dn1 + " is greater than " + dn2)
finally:
        print("--------------------")