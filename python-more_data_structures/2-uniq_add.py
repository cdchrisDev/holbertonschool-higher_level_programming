#!/usr/bin/pyhton3
def uniq_add(my_list=[]):
    res = 0
    new = set(my_list)
    for i in new:
        res += i
    return res
