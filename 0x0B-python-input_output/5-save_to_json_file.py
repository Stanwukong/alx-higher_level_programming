#!/usr/bin/python3
"""This module defines an object-saving function."""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using JSON
    representation.

    Args:
        my_obj (Object): Python object to be serialized and saved.
        filename (str): Path to the text file to store it in.
    """

    with open(filename, 'w') as myObjFile:
        json.dump(my_obj, myObjFile)
