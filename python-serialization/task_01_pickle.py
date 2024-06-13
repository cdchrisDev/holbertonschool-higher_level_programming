#!/usr/bin/python3
"""This is the Pickle custom classes
Module
"""
import pickle


class CustomObject:
    """A base class of simple
    custom obj
    """

    def __init__(self, name,  age, is_student):
        """Instantation
        """

        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """A func to display elem in dict"""

        print("Name: {}\nAge: {}\nIs Student: {}".format(
            self.name, self.age, self.is_student
        ))

    def serialize(self, filename):
        """A func to serialize"""
        return pickle.dump(self, open(filename, "wb"))

    @classmethod
    def deserialize(cls, filename):
        """A func to deserialize"""

        cls = pickle.load(open(filename, 'rb'))
        return cls