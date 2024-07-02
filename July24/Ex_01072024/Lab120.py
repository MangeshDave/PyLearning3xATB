# Abstraction

from abc import ABC, abstractmethod

class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


rect = Rectangle(3, 4)
print(rect.area())

circ = Circle(5)
print(circ.area())
