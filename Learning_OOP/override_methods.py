# ABC is the Abstract class in Python which can't be instanciated, but can be inherited
from abc import ABC


class Shape(ABC):

    def area(self):
        return 0


class Square(Shape):

    def __init__(self, length):
        self.length = length

    def area(self):  # Overridden method
        return self.length * self.length
