#!/usr/bin/python3
"""This is the task_03_countediterator
Module
"""


class CountedIterator():
    """A class that define a new __next__
    Built-in method
    """

    def __init__(self, iterOBJ):
        """Instant"""
        self.iterator = iter(iterOBJ)
        self.cnt = 0

    def get_count(self):
        """Get the count"""
        return self.cnt

    def __next__(self):
        """Mod next"""
        try:
            obj = next(self.iterator)
            self.cnt += 1
            return obj
        except StopIteration:
            raise StopIteration("No more items to iterate")
