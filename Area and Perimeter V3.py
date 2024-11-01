# Area and Perimeter
# Author: Hannah Ludemann
# Date: 2024-11-01
# Version 3


def test_num(question):
    done = False
    while not done:
        print(question) # The 'question is a place holder
        try: # this tries for a valid input
            num = float(input()) # float allows number to be a decimal. input is stored under 'num'
            if num > 0:
                done = True # Stopping the number check
            else:
                print('That is not a valid number. Please try again.')

        except ValueError:
            print('That is not a valid number. Please try again.')

    return(num) # Gives back the value of num so that I can use it outside the function.

keep_going = '' 
while keep_going == '':
    name = input('Hi,what is your name? ')
    print(f'Nice to meet you {name}.')
    width = test_num('Please enter a width more than 0: ')

    height = test_num('Now enter a height more than 0: ')
    print(f'Your two numbers entered are {width} and {height}\n')

    print(f'Calculating area...')
    area = width * height
    print(f'The area of your two numbers is: {area}\n')

    print(f'Calculating perimeter...')
    perimeter = width *2 + height*2
    print(f'The perimeter of your two numbers is: {perimeter}')
    keep_going = input('Press [Enter] to continue or any other key to quit ')