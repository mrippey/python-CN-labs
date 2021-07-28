# Write a lambda expression that takes in three numbers
# and returns the sum of the numbers.
from functools import reduce 


num_list = [1,2,3]

my_lam = reduce(lambda x, y: x+y, num_list)

print(my_lam)