'''1. How to create a file in vs code'''


"""2. How to save the file in vs code?

there are 3 types for save the file in vs code-- CTRL+S, hover over the left upper file directory and save the file and go to setting and auto save the file directory
"""

"""3. How to print Hello World in python"""
print("Hello World!")



'''4. there are 2 types of python comment
1. single line comment.
2. double line comment.
'''
# single line comment.
"""Double line comment"""

# 5. Basic Syntax In Python

# A. comment in python


# B. Indentation in python

if True:
    print("Hello World!")
    print("Debargha Nandi")
print("Dodo")


# C. variable in python (there are several types of variables in python but we need two types in it)

x = 10 # Intiger variables

y = "Debargha" # String variables

print(f"the age of {y} is {x}")


# D. print statement in pthon

a = 10
b = 20

print(a , b)  #automatically there a space in it
print(a , b , sep="@")  # but here we use seperator , thats why 2 numbers can seperate with @

c = "Debargha"
d = "Nandi"

# E. Control Statement
'''control structure in python are used to control the flow of a program , allowing you to make decision'''
'''there are 3 types of control structure
    1. conditional control (if, elif, else)
    2. Iterative control (for, while)
    3. Combination control (nested if, for, while, else)
'''

# 1.1. If Statement

if (10>2):
    print("Hello World!")


# 1.2. if, else statement

if (10>20):
    print("10 is greater than 20")
else:
    print("10 is smaller than 20")


# 1.3. if, elif, else statement

age = 23
if ( age <= 17 ):
    print("you can not drive a car")
elif ( age <= 55 ):
    print("you can drive a car")
else:
    print("You are old")