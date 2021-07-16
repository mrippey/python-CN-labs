# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats():
  # define the function here
  max_nums_in_list = max(example_list)
  min_nums_in_list = min(example_list)
  sum_nums_in_list = sum(example_list)
  average_nums_in_list = sum_nums_in_list / len(example_list)

  print(f'Max: {max_nums_in_list}  Min: {min_nums_in_list}  Sum: {sum_nums_in_list}  Average: {average_nums_in_list}')

# call the function below here
stats()