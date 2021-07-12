'''
import string
from pprint import pprint
import json

def analyze_user_sentence():
    user_sentence = str(input('Enter a sentence: ' ))
    print()
    totals = {}
    lower_case_num = sum(bool(c.islower()) for c in user_sentence)
    upper_case_num = sum(bool(c.isupper()) for c in user_sentence)
    total_sentence_chars = len(user_sentence)
    count = sum(
        user_sentence[i] in ('!', ",", "\'", ";", "\"", ".", "-", "?")
        for i in range(len(user_sentence)))


    totals = {'Lower case': lower_case_num, 'Upper case': upper_case_num, 'Total chars': total_sentence_chars, 'Puncutaion': count}


    for k,v in totals.items():
        print(k, ':' , v)

analyze_user_sentence()
'''

x = 5

y = 10
if x < 5:
    print("one")
elif x > 5:
    print("two")
else:
    print("three")
if x >= 5 and y < 10:
    print("four")
elif x < y and  y == 10:
    print("five")
else:
    print("six")