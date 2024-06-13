#!/usr/bin/python3
"""This is the 10-square
Module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """constructs with size attribute"""
        self.__size = size
        super().__init__(self.__size, self.__size)
        self.integer_validator("size", size)

    def area(self):
        """area method"""
        return self.__size ** 2