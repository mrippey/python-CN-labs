# Print out every prime number between 1 and 1000.


for x in range(2, 1000):
    num_is_prime = all(x % i != 0 for i in range(2, x))
    if num_is_prime:
        print(x)