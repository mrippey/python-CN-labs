# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

'''
text1 = str(input('Enter body of letter info: '))
def write_letter(name, text=text1):

    def greet(name):
        return f'Greetings {name.title()}'

    greeting = f'{greet(name)}'
    goodbye = f'Farewell, {name}'

    #text = str(input('Enter body of letter info: '))

    return f"""{greeting},
    {text}.
{goodbye}"""


print(write_letter('Mike'))
'''

streetno={"1":"Sachin Tendulkar","2":"Sehawag","3":"Dravid","4":"Dhoni","5":"Kohli"}
streetno.update([(v, k) for k, v in streetno.items()])

key = input('Pick a number: ')

result = streetno.get(key)

print(result)