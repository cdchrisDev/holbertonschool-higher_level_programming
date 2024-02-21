#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value += 0
        print("{:d}".format(value))
        return True
    except TypeError:
        return False
