#!/usr/bin/python3
"""This module defines a Square"""


class Square:
    """This represents a square"""

    def __init__(self, size=0):
        """Initializes a new square.
        Args:
            size(optional): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """Returns size of current square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets value of size.
        Args:
            value: value to be given to size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area of current square"""
        return (self.__size ** 2)
