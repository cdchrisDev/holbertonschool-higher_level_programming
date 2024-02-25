#!/usr/bin/python3
"""My square module"""


class Square:
    """Define a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Create a square


        Args:
            size: length of a side
            position: the (x, y) displacement of the square from the left
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """property getter for size"""
        return size.__size

    @property
    def position(self):
        """property getter for position"""
        return self.__position

    @size.setter
    def size(self, value):
        """Property setter for size


        Args:
            value: length of a side

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """Property setter for position

        Args:
            value: A tiple of 2 positive integers defining x and y offset

        Raises: TypeError: If value is not a tuple with 2 elements
        """
        if isinstance(value, tuple) and len(value) == 2:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """calculate the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """print the square of #"""
        if self.__size == 0:
            print()

        XOffset = self.__position[0]
        YOffset = self.__position[1]

        while YOffset > 0:
            print()
            YOffset -= 1

        y = self.__size
        while y > 0:
            x = self.__size
            XOffset = self.__position[0]
            while XOffset > 0:
                print(" ", end="")
                XOffset -= 1
            while x > 0:
                print("#", end="\n" if x == 1 else "")
                x -= 1
            y -= 1
