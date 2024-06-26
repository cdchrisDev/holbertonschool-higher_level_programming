#!/usr/bin/python3
"""This is the 11-student
Module
"""


class Student:
    """A base class student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dict rep of self"""

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

    def reload_from_json(self, json):
        self.first_name = json.get("first_name", "J")
        self.last_name = json.get("last_name", "S")
        self.age = json.get("age", 1)
