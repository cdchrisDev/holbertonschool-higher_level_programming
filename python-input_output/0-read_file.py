#!/usr/bin/python3
"""This is the read_file Module"""


def read_file(filename=""):
    """A func to read file in utf-8"""

    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")