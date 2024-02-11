#!/usr/bin/python3
import string
for letter in string.ascii_lowercase:
    if letter == 'q' or letter == 'e':
        continue
    print(letter, end="")
