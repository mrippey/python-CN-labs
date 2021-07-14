# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

from collections import Counter 

vowel_list = list('aeiou')
vowel_count = {}

get_strng_from_user = str(input('Enter a string: '))


for v in vowel_list:
    count = get_strng_from_user.count(v)
    vowel_count[v] = count

print(vowel_count)