# Use a Python string method to prove which of the following files
# are .pdf files, and which aren't.
# Call the method on each file string and print() Python's response.

file_1 = "operators.pdf"
file_2 = "snowfall.jpg"
file_3 = "uncle-joes-wedding.doc"
file_4 = "invitation.pdf"

group_files = (file_1, file_2, file_3, file_4)

print('PDF files: ')
for x in group_files:
    if x.endswith('.pdf'):
        print(x)

print()
print("Not PDF files: ")
for y in group_files:
    if not y.endswith('.pdf'):
        print(y)