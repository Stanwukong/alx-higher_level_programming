#!/usr/bin/python3
"""Pascal Triangle."""


def pascal_triangle(n):
    """
    Prints n lines of the Pascal Triangle.

    Args:
        n (int): Number of lines to print.

    Return:
        n lines of Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = []

    triangle.append([1])

    for line in range(n - 1):
        last_row = triangle[-1]
        new_row = [1]

        for j in range(len(last_row) - 1):
            new_row.append(last_row[j - 1] + last_row[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
