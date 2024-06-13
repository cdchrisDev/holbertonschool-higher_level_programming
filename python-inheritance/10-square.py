#!/usr/bin/python3
"""This is the 10-square
Module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that define squares
    based on the Rectangle Obj, based
    on BaseGeometry Obj
    """
    
    def __init__(self, size):
        """Constructor
        
        size (int): the size of each side of
        geometrical Obj
        """
        
        self.__size = size
        super().__init__(self.__size, self.__size)
        self.integer_validator("size", size)
        
    def area(self):
        """A func that define the area of a Obj"""
        
        return self.__size ** 2