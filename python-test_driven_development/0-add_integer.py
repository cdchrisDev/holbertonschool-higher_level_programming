#!/usr/bin/python3
def add_integer(a, b=98):
    if isinstance(a, (float, int)) is False:
        raise TypeError("a must be an integer".format(a))
    if isinstance(b, (float, int)) is False:
        raise TypeError("b must be an integer".format(b))
    return int(a) + int(b)
