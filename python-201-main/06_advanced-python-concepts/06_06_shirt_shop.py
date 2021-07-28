# Using a list comprehension, create a *cartesian product* (google this!)
# of the given lists. Then open up your online shop ;)
from itertools import product


colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]


result = [f'{a}{b}' for a, b in product(colors, sizes)]

print(result)