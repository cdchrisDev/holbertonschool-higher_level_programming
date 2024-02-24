#!/usr/bin/python3
"""Square class that prints a square"""


class Square:
    """INIT method init a square class
    Args:
        size: size of square
    """

    def __init__(self, size=0):
        self.size = size

        return self.__size

    @size.setter
    def size(self, value):
        """Sets value to size and checks for errors"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of square
        Return:
           returns the area of the square
        """

        return self.__size = self.__size

    def my_print(self):
        """print square of size '__size' with #"""

        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
