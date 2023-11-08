#!/usr/bin/python3
"""This module defines a function that converts the dictionary of an object."""


def class_to_json(obj):
    """
    Convert data structure to dict.

    Args:
        obj: An instance of a class.

    Return:
        dict: A dictionary representaion of the object.
    """

    obj_attributes = {}

    for attribute, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            obj_attributes[attribute] = value

    return obj_attributes
