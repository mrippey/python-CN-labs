# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.


with open('words.txt', 'r')as rev_words, open('words_reverse.txt', 'w') as new_text:
    word = rev_words.readlines()
    for w in reversed(word):
        new_text.write(w)