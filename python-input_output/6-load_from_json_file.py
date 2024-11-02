#!/usr/bin/python3
"""This is the 6-load_from_json_file
Module
"""
from json import load


def load_from_json_file(filename):
    """A func that creates an Obj from JSON
    File
    """

    with open(filename, 'r', encoding='utf-8') as f:
        return load(f)