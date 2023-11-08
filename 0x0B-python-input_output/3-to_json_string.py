#!/usr/bin/python3
"""This module defines a JSON stringyfier."""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of a object.

    Args:
        my_obj: The object to be serialized.

    Return:
        str: The JSON representation of the object.
    """

    return json.dumps(my_obj)
