# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.

try:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter another number: '))
    result = num1 / num2 
    print(result)

except ValueError:
    print('Numbers (Integers) only please')

except ZeroDivisionError:
    print('Sorry, can\'t divide by zero')