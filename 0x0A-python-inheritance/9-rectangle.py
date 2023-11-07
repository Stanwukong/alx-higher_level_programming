#!/usr/bin/python3
"""This module defines a class Rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """
        Creates instance of Rectangle with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area of the current rectangle."""
        return (self.__width * self.__height)

    def __str__(self):
        """Returns string respresentation of current rectangle."""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
