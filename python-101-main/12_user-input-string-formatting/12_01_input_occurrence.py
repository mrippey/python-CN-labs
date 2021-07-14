# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

recv_a_strng = str(input('Enter a string: '))
recv_a_letter = str(input('Enter a letter: '))
print() 

result = recv_a_strng.find(recv_a_letter)

print(f'String: {recv_a_strng}')
print(f'Letter: {recv_a_letter}')
print(f'Result: {result}')