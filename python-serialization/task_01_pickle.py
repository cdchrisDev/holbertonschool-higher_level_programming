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
        try:
            # return pickle.dump(self, open(filename, "wb"))
            with open(filename, "wb") as Wf:
                pickle.dump(self, Wf)
        except Exception:
            print("Error Pickling")

    @classmethod
    def deserialize(cls, filename):
        """A func to deserialize"""
        try:
            # cls = pickle.load(open(filename, 'rb'))
            with open(filename, "rb") as Rf:
                return pickle.load(Rf)
        except Exception:
            print("Error_depickling")
            return None
