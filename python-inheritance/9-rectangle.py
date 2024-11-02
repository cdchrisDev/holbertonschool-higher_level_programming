#!/usr/bin/python3
"""This is the 9-rectangle
Module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defining a rectangle
    out of basic Geometry
    parent class
    """

    def __init__(self, width, height):
        """init properties of rectangle"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """A func to show area"""
        return self.__width * self.__height

    def __str__(self):
        """A func to return the figure"""
        return f'[Rectangle] {self.__width}/{self.__height}'


if __name__ == '__main__':
    r = Rectangle(3, 5)

    print(r)
    print(r.area())
