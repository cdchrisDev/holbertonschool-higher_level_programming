#!/usr/bin/python3
"""This is write_file Module"""


def write_file(filename="", text=""):
    """A func that writes string to text
    and return the num of chars
    """

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    return len(text)