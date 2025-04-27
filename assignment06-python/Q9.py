#assignment09
# Abstract Classes and Methods Assignment: Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def area(self, length, width):
        return length * width

rectangle = Rectangle()
area = rectangle.area(5, 10)
print(f"The area of the rectangle is: {area}")