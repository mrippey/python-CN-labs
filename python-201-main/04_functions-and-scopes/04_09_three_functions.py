# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

retrieve_nums = int(input('Enter a number: '))

def nested_math_func():
    def inner_power_func(num=retrieve_nums):
        print(f'Inner func power: {num**2}')

        def another_inner_mod_func():
            print(f'Even smaller func modulo: {num % 2}')

        another_inner_mod_func()
    inner_power_func()

nested_math_func()
