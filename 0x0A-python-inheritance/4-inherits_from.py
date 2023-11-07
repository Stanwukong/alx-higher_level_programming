#!/usr/bin/python3
"""This module defines a function that validates an object."""


def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Return:
        bool: True if obj is an instance, otherise False.
    """

    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
