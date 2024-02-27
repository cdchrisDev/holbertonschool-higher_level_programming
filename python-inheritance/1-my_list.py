#!/usr/bin/python3
""" A func to return a sorted list """


class MyList(list):
    """ List of ints """

    def print_sorted(self):
        """ Print MyList"""

        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
