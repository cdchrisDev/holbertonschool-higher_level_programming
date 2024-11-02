#!/usr/bin/python3
"""This is the task_02_verboselits
Module
"""


class VerboseList(list):
    """A class that modify built-in
    methods of list class
    """
    def append(self, obj):
        """Modify append built-in method"""
        super().append(obj)
        print(f"Added [{obj}] to de list.")

    def extend(self, items):
        """Modify extend"""
        super().extend(items)
        print(f"Extended the list with {len(items)} items.")

    def remove(self, obj):
        """Modify remove"""
        super().remove(obj)
        print(f"Revomed {obj} from the list")

    def pop(self, idx=-1):
        """Mod pop"""
        item = super().pop(idx)
        print(f"Popped {item} from the list")
        return item
