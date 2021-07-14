# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

user_number_to_month = int(input('Enter a number between 1 and 12:  '))
print()

if user_number_to_month == 1:
    print("It's January")
elif user_number_to_month == 2:
    print("It's February")
elif user_number_to_month == 3:
    print("It's March")
elif user_number_to_month == 4:
    print("It's April")
elif user_number_to_month == 5:
    print("It's May")
elif user_number_to_month == 6:
    print("It's June")
elif user_number_to_month == 7:
    print("It's July")
elif user_number_to_month == 8:
    print("It's August")
elif user_number_to_month == 9:
    print("It's September")
elif user_number_to_month == 10:
    print("It's October")
elif user_number_to_month == 11:
    print("It's November")
elif user_number_to_month == 12:
    print("It's December")
else:
    print('Error, number not between 1 and 12')
