#!/usr/bin/python3
"""Define 12-pascal_triangle."""


def pascal_triangle(n):
    """Generate Pascal's triangle up to the given number of rows (n)."""
    if n <= 0:
        return []

    triangle = [[1]]

    for m in range(1, n):
        row = [1]
        prev_row = triangle[m - 1]

        for k in range(1, m):
            row.append(prev_row[k - 1] + prev_row[k])

        row.append(1)
        triangle.append(row)

    return triangle
