# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.

file_name = 'integers.txt'

try:
    with open(file_name, 'r')as f:
        content = f.readline().split()
        for line in content:
            if line[0].isdigit():
                result = int(line) / 2
                

except IOError:
    print('File may not exist')

except ZeroDivisionError:
    print('Cannot divide by zero')

else:
    print(result)