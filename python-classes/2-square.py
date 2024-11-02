#!/usr/bin/python3
"""This is the square module"""


class Square:
    """define a square"""

    def __init__(self, size=0):
        """init square"""

        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
