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

    for line in range(n):
        row = [1]
        
        if line > 0:
            last_row = triangle[-1]
            for i in range(len(last_row) - 1):
                row.append(last_row[i - 1] + last_row[i])

                row.append(1)

        triangle.append(row)

    return triangle
