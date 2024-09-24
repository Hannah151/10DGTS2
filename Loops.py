# Lookps and indents
# Author: Hannah Ludemann
# Date: 25 September 2024
# Version: 2
# TODO:
    # Get user input (ask the user for their name)
    # Ask the user for two numbers
    # Add the numbers together

# Ask the user for their name
name = input ('What is your name?')
print(f'Kia ora {name}.') # f stands for format. We are formatting the print statement

# Ask the user for two numbers
num_1 = int(input('What is your favourite number>'))
num_2 = int(input('What is your least favourite number?'))

# Add numbers together
sum = num_1 + num_2 
print(f'The numbers added together equal to {sum}')


# for loops. Repeat for a set number of times.
# for start the loop
# next is the name of the loop
# in range tells the loop how many times to run
# the number in the () is how many times it repeats
for name_of_loop in range (5):
    print('ha!')

# while loop. Runs until a condition is met
keep_going = '' # empty variable
while keep_going == '': 
    print('looping')
    print('still looping')

    keep_going = input('Again? or press any other key to quit')