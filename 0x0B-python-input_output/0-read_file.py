#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """
    Read a text file (UTF-8) ad print it to stdout.

    Args:
        filename (str): The path to the file. Default is an empty string.
    """
    with open(filename, mode="r", encoding="utf-8") as myFile:
        data = myFile.read()
        print(data)
