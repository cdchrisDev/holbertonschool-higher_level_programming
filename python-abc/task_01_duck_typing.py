#!/usr/bin/python3
"""This is the task_01_duck_typing
Module
"""
from abc import ABCMeta, abstractmethod
import math


class Shape(metaclass=ABCMeta):
    """An abstract class that define
    de variations of a Shape class
    """

    @abstractmethod
    def area(self):
        """An abstract method area"""
        pass

    @abstractmethod
    def perimeter(self):
        """An abstract method perimeter
        """
        pass


class Circle(Shape):
    """A class that define Circle
    base on Shape
    """
    def __init__(self, radius):
        """Instan"""
        self.radius = radius

    def area(self):
        """circle radius"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """circle perimeter"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """A class Rectangle base on
    shape
    """
    def __init__(self, width=0, height=0):
        """instant"""
        self.width = width
        self.height = height

    def area(self):
        """Rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Rectangle perimeter"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """A func to print are and perimeter
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
