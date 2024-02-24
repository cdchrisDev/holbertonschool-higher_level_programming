#!/usr/bin/python3
"""Square Class: defines a square as previous classes"""


class Square:
    """Defining a square"""
    def __init__(self, size=0):
        """INIT ATTR"""
        self.size = size

    @property
    def size(self):
        """SIZE GETTER"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size with safe assign"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if (value < 0):
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
