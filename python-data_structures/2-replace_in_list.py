#!/usr/bin/python3
"""2-replace_in_list"""


def replace_in_list(my_list, idx, element):
    """a func to replace on index"""

    if idx < 0 or idx > len(my_list) - 1:
        return my_list

    my_list[idx] = element
    return my_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = -1
    new_element = 4
    new_list = replace_in_list(my_list, idx, new_element)

    print(new_list)
    print(my_list)
