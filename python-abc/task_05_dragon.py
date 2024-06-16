#!/usr/bin/python3
"""This is the task_05_dragon
Module
"""


class SwimMixin():
    """A SwimMixin class"""
    
    def swim(self):
        print("The creature swims!")
        
class FlyMixin():
    """A FlyMixin class"""
    
    def fly(self):
        print("The creature flies!")
        
class Dragon(SwimMixin, FlyMixin):
    """A class that define a dragon
    using Mixin methods
    """
    
    def roar(self):
        print("The dragon roars!")