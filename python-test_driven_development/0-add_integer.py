#!/usr/bin/python3
"""The 0-add_integer module"""


def add_integer(a, b=98):
    """Function adds two integers
    Args:
        a ((int), (float)): first arg
        b ((int), (float)): second arg. Default to 98
        
        return: result op
    
    """
    if isinstance(a, (float, int)) is False:
        raise TypeError("a must be an integer".format(a))
    if isinstance(b, (float, int)) is False:
        raise TypeError("b must be an integer".format(b))
    return int(a) + int(b)
