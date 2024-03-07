#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_ls = a_dictionary.copy()
    key = list(new_ls.keys())
    [new_ls[key[i]]for i in range(len(key))]
    return new_ls
