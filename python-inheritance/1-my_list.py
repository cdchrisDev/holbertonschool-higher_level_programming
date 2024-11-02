#!/usr/bin/python3
"""This is the 1-my_list.py"""


class MyList(list):
    """Define a child list class"""

    def print_sorted(self):
        """A func to print sorted"""

        print(sorted(self))


if __name__ == '__main__':
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
