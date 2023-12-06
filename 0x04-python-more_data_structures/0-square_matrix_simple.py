#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for colu in matrix:
        output = list(map(lambda x: x**2, colu))
        new_matrix.append(output)
    return new_matrix
