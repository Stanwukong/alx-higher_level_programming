#!/usr/bin/python3
"""Defines a module that validates instances of a class."""


def is_same_class(obj, a_class):
    """
    This checks if 'obj' is an instance of 'a_class'.

    Args:
        obj (object): Instance to be validated.
        a_class (Class): Class to be used for validation.

    Return:
        True if obj is an instance of a_class, otherwise false.
    """
    return type(obj) is a_class
