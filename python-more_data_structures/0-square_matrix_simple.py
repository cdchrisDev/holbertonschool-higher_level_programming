#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_ls = matrix[:]
    for x in range(len(new_ls)):
        for i in range(len(new_ls[x])):
            new_ls[x][i] *= matrix[x][i]
    return new_ls
