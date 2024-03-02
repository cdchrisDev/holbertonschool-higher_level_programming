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
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
