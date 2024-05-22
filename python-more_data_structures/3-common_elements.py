#!/usr/bin/python3
"""a func that returns common elements"""


def common_elements(set_1, set_2):
    """return common element in a set"""

    return {x for x in set_1 & set_2} 
