#!/usr/bin/python3
"""This is the task_04_flyingfish
Module
"""


class Fish():
    """A class that define a fish"""
    
    def swim(self):
        print("The fish is swimming")
        
    def habitat(self):
        print("The fish lives in the water")
        
class Bird():
    """A class that define a bird"""

    def fly(self):
        print("The bird is flying")
        
    def habitat(self):
        print("The bird lives in the sky")
        
class FlyingFish(Fish, Bird):
    """A class that define a flying fish
    base on Fish and Bird class
    """
    
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!") 
        
    def habitat(self):
        print("The flying fish lives both in water and the sky!")   