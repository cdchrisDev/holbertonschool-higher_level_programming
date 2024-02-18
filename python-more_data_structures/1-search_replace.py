#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_ls = my_list[:]
    for z in range(len(new_ls)):
        if new_ls[z] == search:
            new_ls[z] = replace
    return new_ls
