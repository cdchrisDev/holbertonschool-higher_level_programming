#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """A func that prints x elements"""
    try:
        y = 0
        for i in my_list:
            y += 1
        z = 0
        for i in my_list:
            if x > y:
                x = y
            if z == x:
                break
            print("{}".format(i), end="")
            z += 1
        print()
    except IndexError:
        print("out of range")
    return x


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
