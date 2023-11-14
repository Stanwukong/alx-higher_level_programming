#!/usr/bin/python3
"""This module definess a class Rectangle."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a rectangle.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x: X-coordinate of the rectangle's position.
            y: Y-coordinate of the rectangle's position.

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns the width."""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width attribute."""
        self.__width = width

    @property
    def height(self):
        """Returns the height."""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height attribute."""
        self.__height = height

    @property
    def x(self):
        """Returns X-coordinate."""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets the X-coordinate."""
        self.__x = x

    @property
    def y(self):
        """Returns Y-coordinate."""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the Y-coordinate."""
        self.__y = y
