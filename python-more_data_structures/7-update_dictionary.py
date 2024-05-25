#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if not isinstance(key, str):
        raise TypeError("non-string key")

    a_dictionary[key] = value

    return a_dictionary