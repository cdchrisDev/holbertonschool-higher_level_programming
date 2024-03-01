#!/usr/bin/python3
"""
A class Inherited from the moduls.base module
"""

from models.base import Base


class Rectangle(Base):
    """
    Almost a copy of base, but we call it
    inheritance
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Base now has attr of rectangles accordingly
        """
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
