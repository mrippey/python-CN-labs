# Create a script that asks a user to input an integer, checks for the
# validity of the input type, and displays a message depending on whether
# the input was an integer or not.
# The script should keep prompting the user until they enter an integer.

#input_num = input('Enter a number: ')

import sys 


def request_an_int():
    get_user_int = input('Enter a num: ')


    while True:
        if get_user_int.isdigit() == True:
            print('Thanks')
            break
        else:
            request_an_int()

request_an_int()