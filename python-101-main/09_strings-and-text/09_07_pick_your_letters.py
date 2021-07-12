# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "

we_from_word = word[1:3]

see_from_word = word[-2] + word[2:4]

trees_from_word = word[0] + word[-3] + word[2:4] + word[-2]

new_sentence = we_from_word + ' ' + see_from_word + ' ' + trees_from_word

print(new_sentence)