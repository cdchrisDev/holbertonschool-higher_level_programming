#!/usr/bin/python3
"""1-element_at"""


def element_at(my_list, idx):
    """A fun that retrieves an element from a list
    """

    if idx < 0 or idx > len(my_list):
        return None
    cnt = 0
    for i in my_list:
        if cnt == idx:
            return i
        else:
            cnt += 1


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
