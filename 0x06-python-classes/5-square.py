#!/usr/bin/python3
"""This module defines a Square class"""


class Square:
    """This represents a square"""
    def __init__(self, size=0):
        """This initializes the square instance.
        Args:
            size(optional): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """Returns the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets value to the size of the square.
        Args:
            value: value to be attributed to size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of current square"""
        return (self.__size ** 2)

    def my_print(self):
        """prints the square with # to stdout"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
