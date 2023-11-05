#!/usr/bin/python3
"""This module defines a function that prints a square with the character #."""


def print_square(size):
    """
    Prints a square with size length of sides

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer or if it's a float less than 0.
        ValueError: If size is less than 0.
    """
    err_mssg1 = "size must be an integer"
    err_mssg2 = "size must be >= 0"

    if not isinstance(size, int):
        raise TypeError(err_mssg1)

    if isinstance(size, float) and size < 0:
        raise TypeError(err_mssg1)

    if size < 0:
        raise ValueError(err_mssg2)

    for i in range(size):
        print("#" * (size))
