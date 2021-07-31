'''Instructions
Write a decorator function that wraps text passed to it in a specified HTML tag. The user should be able to decide which tag to use.
'''

def html_tag_some_text(tag):
    def decorator_func(func):
        def wrapper(*args):
            print(f'<{tag}> {func(*args)} </{tag}>')
        return wrapper 
    return decorator_func


@html_tag_some_text('b')
def text_to_bold_tag(txt):
    return txt 

text_to_bold_tag('hello')


@html_tag_some_text('h1')
def text_to_header_tag(txt2):
    return txt2 