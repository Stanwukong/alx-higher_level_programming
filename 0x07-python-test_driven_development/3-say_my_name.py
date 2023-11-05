#!/usr/bin/python3
"""This module defines a function that prints strings"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    err_mssg1 = "first_name must be a string"
    err_mssg2 = "last_name must be a string"

    if not isinstance(first_name, str):
        raise TypeError(err_mssg1)
    if not isinstance(last_name, str):
        raise TypeError(err_mssg2)

    print("My name is {} {}".format(first_name, last_name))
