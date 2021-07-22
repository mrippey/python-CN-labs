# Write a script that generates an exception.
# Handle this exception with a try/except block.
# For example:
#
# list_ = ["hello world!"]
# print(list_[1])
#
# This raises and exception that needs to be handled.

'''
example = 'This is just a test'

print(example.keys())
'''

try:
    example = 'This is just a test'
    print(example.keys())
except AttributeError as err:
    print(f'Error: {err}')