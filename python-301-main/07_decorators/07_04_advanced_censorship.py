# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".


def censor(w1, w2):
    def censorship(func):
        def wrapper():
            print(func().replace(w1, '****').lower().replace(w2, '****').lower())
        return wrapper 
    return censorship

@censor('shoot', 'crab')
def wash_your_mouth_out():
    return 'I stabbed my toe on a crab! Oh shoot!'

wash_your_mouth_out()
