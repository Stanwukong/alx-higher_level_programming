#!/usr/bin/python3
"""This module defines a function that converts JSON to an Object."""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Return:
        obj: The object created from the JSON file.
    """

    with open(filename, "r") as myFile:
        return json.load(myFile)
