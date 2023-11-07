#!/usr/bin/python3
"""This module contains a function called lookup."""


def lookup(obj):
    """
    This function lists the available attributes and
    methods of an object.

    Args:
        obj (object): Object to be checked.

    Return:
        list (object): List of available attributes and methods of 'obj'.
    """
    list = dir(obj)

    return list
