#!/usr/bin/python3
"""This is the serialization Module"""
from json import dumps, dump, load, loads

def serialize_and_save_to_file(data, filename):
    """A func that serialize and save to file
    Args:
        data(dict): data to serialize
        filename(str): JSON output
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(dumps(data))


def load_and_deserialize(filename):
    """A func from JSON to obj
    Args:
        filename(str): JSON input
    """

    with open(filename, 'r', encoding="utf-8") as f:
        return load(f)