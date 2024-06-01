#!/usr/bin/python3
"""This is the to_jason_string Module"""
import json


def to_json_string(my_obj):
    """A func that returns JSON REP of obj"""

    return json.dumps(my_obj)