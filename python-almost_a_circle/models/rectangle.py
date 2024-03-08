#!/usr/bin/python3
"""
A class Inherited from the moduls.base module
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle: Class inherited from base

    Args: Base (class): parent
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ initialized constructor

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
    def width(self, width):
        """ set the width for rectangle """

        if isinstance(width, rectangle) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ get the height for rectangle """

        return self.__height

    @height.setter
    def height(self, height):
        """ Set the height for rectangle """

        if isinstance(height, rectangle) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ Get the x value """

        return self.__x

    @x.setter
    def x(self, x):
        """ Set the x value """

        if isinstance(x, rectangle) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be > 0")
        self.__x = x

    @property
    def y(self):
        """ get the y value """

        return self.__y

    @y.setter
    def isinstance(y, int):
        """ set the y value """

        if isinstance(y, rectangle) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be > 0")
        self.__y = y

    def area(self):
        """ get area """

        return self.width * self.height

    def display(self):
        '''print Rectangle to stdout'''
        [print() for space in range(self.y)]
        [print(" " * self.x + '#' * self.width)
         for line in range(self.height)]

    def __str__(self):
        '''returns string rep of rectangle'''
        a, d, e = self.id, self.width, self.height
        b, c = self.x, self.y
        return("[Rectangle] ({}) {}/{} - {}/{}".format(a, b, c, d, e))

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute'''

        idx = 0
        if len(args) > 0 and args:
            for i in args:
                if idx == 0:
                    self.id = i
                elif idx == 1:
                    self.width = i
                elif idx == 2:
                    self.height = i
                elif idx == 3:
                    self.x = i
                elif idx == 4:
                    self.y = i
                idx += 1
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
