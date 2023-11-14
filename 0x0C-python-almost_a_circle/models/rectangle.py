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
        if not isinstance(width, int):
             raise TypeError("width must be an integer.")
        elif width <= 0:
             raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Returns the height."""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height attribute."""
        if not isinstance(height, int):
             raise TypeError("height must be an integer.")
        elif height <= 0:
             raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Returns X-coordinate."""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets the X-coordinate."""
        if not isinstance(x, int):
             raise TypeError("x must be an integer")
        if x < 0:
             raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Returns Y-coordinate."""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the Y-coordinate."""
        if not isinstance(y, int):
             raise TypeError("y must be an integer.")
        if y < 0:
             raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area of thr Rectangle instance."""
        return self.__height * self.__width

    def display(self):
        """Prints # to stdout to represent the rectangle instance."""
        for line in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """Returns string representaion of instance."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
