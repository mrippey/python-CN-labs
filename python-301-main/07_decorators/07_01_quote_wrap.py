# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.


def wrap_me_up(func):
    def wrapper():
        original_text = func()
        quoted_text = f'"{original_text}"'
        return quoted_text
    return wrapper

@wrap_me_up
def some_quote():
    return 'To be, or not to be, --William Shakespeare '

print(some_quote())