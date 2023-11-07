#!/usr/bin/python3
"""This modules contains a function that validates instances of a class."""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of, or instance of a derived class of a_class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Return:
        bool: True is obj is an instance of a_class, otherwise False.
    """

    return (isinstance(obj, a_class))
