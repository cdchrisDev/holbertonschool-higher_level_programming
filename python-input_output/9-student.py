#!/usr/bin/python3
"""This is the 9-students
Module
"""

class Student():
    """This is a base class Student"""

    def __init__(self, first_name, last_name, age):
        """Init of class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """a Func that retrieves a json rep"""

        return self.__dict__