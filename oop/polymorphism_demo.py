# polymorphism_demo.py
import math

# Base Class
class Shape:
    def area(self):
        """Base method that should be overridden in subclasses."""
        raise NotImplementedError("Subclasses must override the area() method")


# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of a rectangle."""
        return self.length * self.width


# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Calculate and return the area of a circle."""
        return math.pi * (self.radius ** 2)
