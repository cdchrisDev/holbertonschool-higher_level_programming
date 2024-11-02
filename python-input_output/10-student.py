#!/usr/bin/python3
"""This is the 10-student
Module
"""


class Student():
    """This is the base class student"""

    def __init__(self, first_name, last_name, age):
        """instantation"""
        first_name = self.first_name
        last_name = self.last_name
        age = self.age

    def to_json(self, attrs=None):
        """Retrieves dict rep of json"""
        
        ret_dict = {}
        if type(attrs) is list:
            for item in attrs:
                if type(item) is not str:
                    return self.__dict__
            for key in attrs:
                if key in self.__dict__:
                    ret_dict.update({key: self.__dict__[key]})
            return ret_dict
        else:
            return self.__dict__