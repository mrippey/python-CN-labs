# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

get_num_from_user = int(input('Enter a number between 1 and 1,000,000,000 (no commas):  '))
print() 

while True:
    if get_num_from_user % 3 == 0:
        print(f'Num {get_num_from_user} is divisible by three, thanks.')
        break

    else:
        get_num_from_user = int(input('Enter a number between 1 and 1,000,000,000 (no commas):  '))
        print()