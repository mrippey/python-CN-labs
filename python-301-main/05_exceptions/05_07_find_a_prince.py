# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".

import os 
import pathlib as pth

 
war_and_peace = pth.Path('books/war_and_peace.txt')
pride_and_pred = pth.Path('books/pride_and_prejudice.txt')
crime_and_pun = pth.Path('books/crime_and_punishment.txt')


class PrinceException(Exception):
    def __init__(self, pths):
        self.pths = pths
        self.message = f'Found a prince in {self.pths}'


with open(war_and_peace, 'r')as file1, open(pride_and_pred, 'r')as file2, open(crime_and_pun, 'r')as file3:

    content1 = file1.readline().splitlines()
    content2 = file2.readline().splitlines()
    content3 = file3.readline().splitlines()

pths = (content1, content2, content3)
a, b, c = pths

try:
    if "Prince" not in a[0:100] or "Prince" not in b[0:100] or "Prince" not in c[0:100]:
        
        raise PrinceException(pths)
except PrinceException as pe:
    print(pe.message)
        



#if ("Prince") in *[0:100]: # do something
'''

a, b, c = pths 
print(a)
print(b)
print(c)
'''