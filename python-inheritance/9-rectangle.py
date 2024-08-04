#!/usr/bin/python3
'''
Write a class Rectangle
that inherits from BaseGeometry (7-base_geometry.py).
(task based on 8-rectangle.py)
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class base on BaseGeometry"""
    def __init__(self, width, height):
        super().integer_validator('width', width)
        self.__width = width
        super().integer_validator('height', height)
        self.__height = height

    def area(self):
        """Area func return obj area"""
        return self.__width * self.__height

    def __str__(self):
        """String rep of sizes"""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
