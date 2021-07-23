# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?

import os 

# Task 1)
with open('books/war_and_peace.txt', 'r')as io:
    content = io.readlines()  
    
# Task 2)
    with open('books/crime_and_punishment.txt', 'w')as ow:
        ow.write(' ')  


#Task 3)
try:
    with open('books/war_and_peace.txt', 'r')as file1:

        content1 = file1.readline().splitlines()

        for y in content1:
            print(y[0])

        with open('books/pride_and_prejudice.txt', 'r')as file2:
            content2 = file2.readline().splitlines()
            
            for z in content2:
                print(z[0])

        file_path = 'books/crime_and_punishment.txt'
        with open(file_path, 'r')as file3:
            
            content3 = file3.readline().splitlines()

            for a in content3:
                print(a[0])

except IOError as err:
    print(f'Error: {err} ')