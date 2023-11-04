#!/usr/bin/python3

"""This module defines a square"""


class Square:
    """This represents a square"""

    def __init__(self, size=0):
        """Initializes the Square class
        Args:
            size(optional): size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        Methods:
            area(public): returns the current square area
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the current square"""
        return (self.__size ** 2)
