#!/usr/bin/python3
"""This module defines a class BaseGeometry."""


class BaseGeometry:
    """
    BaseGeometry class with area and integer_validator methods.
    """

    def area(self):
        """Raises Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an integer value.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
