#!/usr/bin/python3
"""This module defines a file-appending function."""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF-8)

    Args:
        filename (str): The path of the file to be appended. Default is empty.
        text (str): The text to be appended. Default is empty.

    Return:
        int: The number of characters added.
    """

    with open(filename, "a", encoding="utf-8") as myFile:
        num_of_chars = myFile.write(text)

    return num_of_chars
