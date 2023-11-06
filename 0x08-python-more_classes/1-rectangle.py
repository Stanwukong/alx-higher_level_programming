#!/usr/bin/python3
"""This module defines a Rectangle class with properties"""


class Rectangle:
    """This class represents a rectangle"""

    def __init__(self, width=0, height=0):
        """
        This instantiates an object of this class.

        Args:
            width (int, optional): The width of the object. Defaults to 0.
            height (int, optional): The height of the object. Defaults to 0.
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
        """Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
