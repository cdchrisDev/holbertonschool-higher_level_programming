#!/usr/bin/python3
"""This is the task_02_verboselits
Module
"""


class VerboseList(list):
    """A class that modify built-in
    methods of list class
    """
    def append(self, obj):
        super().append(obj)
        print(f"Added [{obj}] to de list.")
    
    def extend(self, items):
        super().extend(items)
        print(f"Extended the list with {len(items)} items.")
    
    def remove(self, obj):
        super().remove(obj)
        print(f"Revomed {obj} from the list")
    
    def pop(self, idx=-1):
        item = super().pop(idx)
        print(f"Popped {item} from the list")
        return item    
    