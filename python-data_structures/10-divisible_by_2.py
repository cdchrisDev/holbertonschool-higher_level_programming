#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_ls = my_list[:]
    for i in my_list:
        if my_list[i] % 2 == 0:
            new_ls[i] = True
        else:
            new_ls[i] = False

    return new_ls
