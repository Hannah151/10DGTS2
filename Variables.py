# Showing how variables work
# Author: Hannah Ludemann
# Date: 20 September 2024
# Version: 1


# Different types of variables
num_1 = 44 # Assigning 44 to num_1
print(num_1) # This displays what num_1 contains


# Store a string
name = 'Hannah'
print(name) # This displays what 'name' contains
name = 'aaskjdha' # reassinging value to an existing variabble
print(name)

# Do calculations in a variable and store the result
sum=5+5 # not good practice
sum = 5 + 5 # follows PEP8 Python conventions
print(sum)
sum_string = '5 + 5 = 10' # this is a string
print(sum_string)

# adding strings together is called concatenation
concatenation = name + sum_string
print(concatenation)