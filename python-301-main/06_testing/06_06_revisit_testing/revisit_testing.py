# Revisit one of the previous lab exercises that were challenging for you.
# Write a test suite that checks for the correct functionality of the code.
# Then try to refactor your solution, maybe you can make the code more
# concise or more elegant? Keep checking whether you broke the functionality
# by repeatedly running your test suite against your changes.


def get_driver_information(distance, liters, fuel_price):

    try:

        trip_total_cost = distance / liters * fuel_price

        return f'The total cost of your trip is €{trip_total_cost:.2f}'

    except ZeroDivisionError as er:
        print(f'Run-time error: {er}')
        


print(get_driver_information(300, 12, 3.12))
