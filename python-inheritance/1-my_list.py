#!/usr/bin/python3
"""This is the 1-my_list
Module
"""


class MyList(list):
    """This is a class that Define
    MyList: Inherited from 'list'
    """
    
    def print_sorted(self):
        print(sorted(self))