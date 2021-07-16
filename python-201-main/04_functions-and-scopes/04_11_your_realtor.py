# Write a function that prints out nicely formatted information about a
# real estate listing. The information can vary for every listing, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.


def real_estate_listing(**kwargs):
    for k, v in kwargs.items():
        print(f'{k} in nice area with {v}')


real_estate_listing(Home = 'great views by the sea', Apartment='two bedrooms and walk in closets')