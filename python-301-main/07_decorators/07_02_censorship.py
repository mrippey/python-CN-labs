# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"


def censorship(func):
    def wrapper():
        print(func().replace('Shoot', 'S****'))
    return wrapper 

@censorship
def wash_your_mouth_out():
    return 'I bumped my toe! Shoot!'

wash_your_mouth_out()