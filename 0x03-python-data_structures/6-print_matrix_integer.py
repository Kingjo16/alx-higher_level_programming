#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line_row in matrix:
        for line_col in line_row:
            print("{:d}".format(line_col), end=" " if line_col != line_row[-1] else "")
        print()
