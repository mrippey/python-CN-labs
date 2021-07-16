# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages

pick_a_number = int(input('Enter a number between 1 and 1,000,000,000:  '))
print()

def div_by_four_or_seven(num=pick_a_number):
    return bool(num % 4 or 7 == 0) 

new_var1 = div_by_four_or_seven()
print(new_var1)

def div_by_four_and_seven(num=pick_a_number):
    return bool(num % 4 and 7 == 0) 

new_var2 = div_by_four_and_seven()
print(new_var2)