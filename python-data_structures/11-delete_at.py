#!/usr/bin/python
def delete_at(my_list=[], idx=0):
    length = len(my_list)

    if idx < 0 or idx >= length:
        return (my_list)

    del my_list[idx]

    ºreturn (my_list)
