# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

a,b,c=input("Enter two characters separated by space:").split()

longest = max(a,b,c, key=len)

print(f'{len(longest)}, {longest}')