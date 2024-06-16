#!/usr/bin/python3
"""This is the task__00_abc
Module
"""
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    """An abstract class that define
    variations for animal from
    ABCMeta
    """
    @abstractmethod
    def sound(self):
        """A general sound method"""
        pass


class Dog(Animal):
    """A class that define a Dog base
    on Animal class
    """

    def sound(self):
        """The sound of dog"""
        return "Bark"


class Cat(Animal):
    """A class that define a cat base
    on Animal class
    """

    def sound(self):
        """The sound of cat"""
        return "Meow"
