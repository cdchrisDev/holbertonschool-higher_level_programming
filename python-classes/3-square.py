#!/usr/bin/python3
"""A class defined as 'Square'"""


class Square:
    """defining a square as class"""
    def __init__(self, size=0):
        """start"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """area of a square"""
        return (self.__size) ** 2
    # area func declare as public with same indented space as __init__
