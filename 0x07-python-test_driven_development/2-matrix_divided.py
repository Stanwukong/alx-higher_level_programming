#!/usr/bin/python3

"""This module defines a matrix division function"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor.

    Returns:
        list of lists: The result of the division in a new matrix.
    Raises:
        TypeError: If matrix is not a list of lists of integers or floats
                   If each row of matrix is not the same size
                   If div is not a number
        ZeroDivisionError: If div is equal to 0
    """
    err_mssg1 = "matrix must be a matrix (list of lists) of integers/floats"
    err_mssg2 = "Each row of the matrix must have the same size"
    err_mssg3 = "div must be a number"
    err_mssg4 = "division by zero"

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(err_mssg1)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(err_mssg1)
        for item in row:
            if not isinstance(item, (float, int)):
                raise TypeError(err_mssg1)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError(err_mssg2)

    if not isinstance(div, (int, float)):
        raise TypeError(err_mssg3)

    if div == 0:
        raise ZeroDivisionError(err_mssg4)

    new_matrix = []

    for item in matrix:
        row = []
        for list_num in item:
            row.append(round((list_num / div), 2))
        new_matrix.append(row)

    return (new_matrix)
