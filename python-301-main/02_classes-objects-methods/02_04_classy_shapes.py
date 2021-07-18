# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.

class Rectangle():

    def __init__(self, rec_length, rec_width):
        self.rec_length = rec_length
        self.rec_width = rec_width

    def rectangle_area(self):
        print(f'Rectangle Area: {self.rec_length * self.rec_width}')

    def rectangle_perimeter(self):
        print(f'Rectangle Perimeter: {2*(self.rec_length + self.rec_width)}')

r = Rectangle(10, 13)
r.rectangle_area()
r.rectangle_perimeter()

class Circle():
    print()
    def __init__(self, circle_radius):
        self.circle_radius = circle_radius


    def circle_area(self):
        print(f'Circle Area: {3.14 * self.circle_radius**2}')

    def circle_circumference(self):
        print(f'Circle Circumference: {2 * 3.14 * self.circle_radius:.2f}')

c = Circle(5)
c.circle_area()
c.circle_circumference()