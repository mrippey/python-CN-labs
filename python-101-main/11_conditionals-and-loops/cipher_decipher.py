'''
Replicate one of the oldest known encryption in code.

Apply a Cesar cipher of 7 to the 'secret' variable.

'''

secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7



def decipher_the_cipher(text = secret, shift_num = cipher):
    result = ""
    for char in text:
        if char == '':
            result += char
        elif char.isupper():
            result += chr((ord(char) + shift_num - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift_num - 97) % 26 + 97)

    return result 

solution = decipher_the_cipher()       
print(f'Input: {secret}')
print(f'Shift Number: {cipher}')
print(f'Result: {solution}')