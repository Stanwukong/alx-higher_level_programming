#!/usr/bin/python3

"""This module defines a square"""


class Square:
    """This class represents a square"""

    def __init__(self, size=0):
        """Initializes the Square class

        Args:
            size(optional): size of the new square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
