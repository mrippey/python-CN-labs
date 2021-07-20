# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).


with open('words.txt', 'r')as twenty_char:
    words  = []
    for text in twenty_char.readlines():
        text = text.rstrip()
        if len(text) == 20:
            words.append(text)
    print(words)


'''
with open('words.txt', 'r')as out:
    far_list = []
    for word in out.readlines():
        word = word.rstrip()
        if word.startswith('far'):
            far_list.append(word)
    print(far_list)
'''

 