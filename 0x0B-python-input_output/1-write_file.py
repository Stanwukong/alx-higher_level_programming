#!/usr/bin/python3
"""This module defines a text-file line-counting function."""


def write_file(filename="", text=""):
    """
    Write a string to a text file and return
    the number of characters written.

    Args:
        filename (str): The path to the file. Default is an empty string.
        text (str): The text to be written to the file. Default is empty.

    Return:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf=8") as myFile:
        no_of_chars = myFile.write(text)
    return no_of_chars
