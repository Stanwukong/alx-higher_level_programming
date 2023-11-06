#!/usr/bin/python3
"""This module defines a Rectangle."""


class Rectangle:
    """This represents a rectangle."""

    def __init__(self, width=0, height=0):
        """
        This instantiates an object of this class.

        Args:
            width (int, optional): The width of the rectangle.
            height (int, optional): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area."""
        return (self.__height * self.__width)

    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width + self.__height) * 2)

    def __str__(self):
        """
        Generate a string representation of the rectangle using '#'.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join(['#' * self.__width for i in range(self.__height)]))
