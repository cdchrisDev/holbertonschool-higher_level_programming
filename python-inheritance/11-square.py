#!/usr/bin/python3
'''import class'''


Rectangle = __import__('9-rectangle').Rectangle
'''class'''


class Square(Rectangle):
    '''method'''
    def __init__(self, size):
        '''validator'''
        self.integer_validator("size", size)
        '''method super class'''
        super().__init__(size, size)
        """Asign proper priv var"""
        self.__size = size

    def area(self):
        """Give the obj area"""
        return self.__size ** 2
    
    def print(self):
        """print the obj size"""
        print(f"[Square] <{self.__size}/{self.__size}")

    def str(self):
        """return the str rep of obj"""
        return f"[Square] <{self.__size}/{self.__size}"
