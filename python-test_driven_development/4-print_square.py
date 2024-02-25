#!/usr/bin/python3
"""4-print_square module"""


def print_square(size):
    """print a square of size with #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    print(f"{('#' * size + chr(10)) * size}", end="")
