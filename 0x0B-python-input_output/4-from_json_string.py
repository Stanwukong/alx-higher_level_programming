#!/usr/bin/python3
"""This module defines a JSON decoder."""
import json


def from_json_string(my_str):
    """
    This coverts a JSON string into a python object.

    Args:
        my_str (str): This is the string to be converted.

    Return:
        my_obj (object): Python object data structure.
    """

    my_obj = json.loads(my_str)

    return my_obj
