# Use the built-in `sys` module to explicitly quit your script.
# Include this functionality into a loop where you're asking the user
# for input in an infinite `while` loop.
# If the user enters the word "quit", you can exit the program
# using a functionality provided by this module.

import sys

def infinity_question():
    get_user_input = str(input("Enter something witty: "))

    while True:
        if get_user_input == 'quit':
            sys.exit()
        else:
            infinity_question()

infinity_question()