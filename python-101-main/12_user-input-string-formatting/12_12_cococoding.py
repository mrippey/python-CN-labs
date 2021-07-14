# Write the necessary code to display the follow message to the console
#       Time for co-co-co-ding.
# Use an operator and f-string formatting to create this output


test_for_code = 'Time for coding'

get_letters = test_for_code[8:11]

solution = get_letters.replace(' ', '-')*3

print(f'Time for co{solution}ding.')