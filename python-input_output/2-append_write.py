#!/usr/bin/python3
"""This is the append_write Module"""


def append_write(filename="", text=""):
    """A func that appendas string at the end
    and returns num of chars
    """

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)

    return len(text)