#!/usr/bin/python3
""" defines a rectangle """


class Rectangle:
    """ defining a rectangle"""

    def __init__(self, width=0, height=0):
        """ INIT rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """ Returns the periimeter of rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """ prints the new rectangle """
        if self.__height == 0 or self.__width == 0:
            return ""
        return (("#" * self.__width + "\n") * self.__height).strip("\n")

    def __repr__(self):
        """ Returns the representation of the rectangle """
        return f"Rectangle({self.width}, {self.height})"
