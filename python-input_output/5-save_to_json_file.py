#!/usr/bin/python3
"""This is the 5-save_to_json_file
Module
"""
from json import dumps


def save_to_json_file(my_obj, filename):
    """A func tahta writes an Obj
    to text file, using JSON rep
    """

    with open(filename, 'w') as f:
        f.write(dumps(my_obj))
