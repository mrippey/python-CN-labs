# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.


text1 = str(input('Enter body of letter info: '))
def write_letter(name, text=text1):
    greet = f'Dear {name}'
    goodbye = f'Farewell, {name}'

    #text = str(input('Enter body of letter info: '))

    return f"""{greet},
    {text}.
{goodbye}"""


print(write_letter('Mike'))