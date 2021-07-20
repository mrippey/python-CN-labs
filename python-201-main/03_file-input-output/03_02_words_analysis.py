# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.


number_of_words = 0

with open('words.txt', 'r') as find_words:
    word = find_words.read().split()
    number_of_words += len(word)
    max_len_word = max(word, key=len)
    short_len_word = min(word, key=len)
    
    print(f'Shortest word: {short_len_word}')
    print(f'Longest word: {max_len_word}')
    print(f'Total number of words: {number_of_words}')
