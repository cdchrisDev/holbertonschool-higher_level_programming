#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_ls = a_dictionary.copy()
    key = list(new_ls.keys())
    for i in range(len(key)):
        new_ls[key[i]] = new_ls[key[i]] * 2
    return new_ls
