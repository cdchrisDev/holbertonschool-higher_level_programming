#!/usr/bin/python3
"""
Divides a matrix
"""


def matrix_divided(matrix, div):
    """
    Function that divides a matrix
    """

    if type(matrix) != list:
        raise TypeError("matrix must be a matrix(list of list) of
                        integers/floats")
    for item in range(len(matrix)):
        if item != 0:
            result = item - 1
            if len(matrix[item]) != len(matrix[result]):
                raise TypeError("Each row of the matrix
                                must have the same size")
    if isinstance(div, int) is False:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(item / div, 2) for item in m_list] for m_list in matrix]
