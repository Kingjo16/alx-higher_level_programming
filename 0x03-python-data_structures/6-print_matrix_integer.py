#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lie_row in matrix:
        for lie_col in lie_row:
            print("{:d}".format(lie_col), end=" " if lie_col != lie_row[-1] else "")
        print()
