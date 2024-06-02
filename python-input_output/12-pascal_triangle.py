#!/usr/bin/python3
"""The 12-pascal_triangle
Module
"""


def pascal_triangle(n):
    """Return a list of list of ints the pascal
    triangle
    """

    triangle = []
    if n <= 0:
        return triangle
    for row in range(n):
        new_row = []
        triangle.append(new_row)
        new_row.append(1)
        for col in range(1, row):
            new_row.append(triangle[row - 1][col - 1] + triangle[row - 1][col])
        if row > 0:
            new_row.append(1)
    return triangle