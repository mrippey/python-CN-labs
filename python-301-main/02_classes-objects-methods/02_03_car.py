# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.

class Car():
    '''Set attributes for car'''
    def __init__(self, model, year, color, max_speed=0, current_mileage=0, good_tires=0):
        self.model = model 
        self.year = year 
        self.max_speed = max_speed
        self.current_mileage = current_mileage
        self.color = color
        self.good_tires = good_tires

    def __repr__(self):
        '''Use __repr__ to print details of car'''
        return f"""Car: {self.model}, Year: {self.year}, Max Speed: {self.max_speed}, Miles: {self.current_mileage}, Color: {self.color}
        Good tires: {self.good_tires}"""

    def accelerate(self):
        '''Add five to max_speed each time accelarate method is called'''
        self.max_speed += 5

    def brake(self):
        '''Subtract five from max_speed each time brake method is called'''
        if self.max_speed == 0:
            self.max_speed = 0
        else:
            self.max_speed -= 5

    def paint_job(self, new_color):
        self.new_color = new_color
        print(f'Old color: {self.color} New color: {self.new_color}')

    def take_a_drive(self):
        self.current_mileage += 100

    def honk_horn(self):
        '''Return sound of horn from car'''
        print(f"{self.model} goes 'beep beep'")

