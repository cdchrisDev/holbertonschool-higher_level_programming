#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_ls = [x[:] for x in matrix]
    for x in range(len(matrix)):
        for i in range(len(matrix[x])):
            new_ls[x][i] = new_ls[x][i] ** 2
    return new_ls
