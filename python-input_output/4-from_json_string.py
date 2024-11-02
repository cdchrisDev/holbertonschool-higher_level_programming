#!/usr/bin/python3
"""This is the 4-from_json_string
Module
"""
from json import loads


def from_json_string(my_str):
    """A func that returns an object"""

    return loads(my_str)