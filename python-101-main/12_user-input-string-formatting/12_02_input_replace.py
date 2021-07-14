# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

recv_a_strng = str(input('Enter a string: '))
recv_a_symbol = str(input('Enter a letter: '))
print() 

result = recv_a_strng.replace(recv_a_strng[0], recv_a_symbol)

print(f'String input: {recv_a_strng}')
print(f'Letter input: {recv_a_symbol}')
print(f'Result: {result}')