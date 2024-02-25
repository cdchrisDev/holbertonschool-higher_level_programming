#!/usr/bin/python3
""" Defining a Rectangle """


class Rectangle:
    """ Defining a rectangle """

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
        """ Setting values for rectangle """
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
        """ sets the height of new rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height mus be >= 0")
        self.__height = value
