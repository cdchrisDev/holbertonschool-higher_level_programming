#!/usr/bin/python3
"""
A class Inherited from the moduls.base module
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle: Class inherited from base

    Args: Base (class): parent
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        __init__ initialized constructor

        Args:
            width (int)
            height (int)
            x (int): default 0
            y (int): default 0
            id ([type]): Default None
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            """ Width getter for rectangle """
            return self.__width

        @width.setter
        def width(self, value):
            """ set the width for rectangle """
            self.__width = value

        @property
        def height(self):
            """ get the height for rectangle """
            return self.__height

        @height.setter
        def height(self, value):
            """ Set the height for rectangle """
            self.__height = value

        @property
        def x(self):
            """ Get the x value """
            return self.__x

        @x.setter
        def x(self, value):
            """ Set the x value """
            self.__x = value

        @property
        def y(self):
            """ get the y value """
            return self.__y

        @y.setter
        def y(self, value):
            """ set the y value """
            self.__y = value
