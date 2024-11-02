#!/usr/bin/python3
"""This is the data structure
Module
"""


def print_list_integer(my_list=[]):

    """A func to print list of ints"""
    for i in my_list:
        print("{:d}".format(i))

    print(end="")


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_list_integer(my_list)
