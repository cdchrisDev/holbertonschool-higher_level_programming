#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    div = number % 10
    print("{0:d}".format(div), end="")
    return (div)
