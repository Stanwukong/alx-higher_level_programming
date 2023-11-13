#!/usr/bin/python3
"""This module defines a class Base."""


class Base:
    """
    Base class for managing id attributes
    for all classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor.

        Args:
            id (int or None): The id of the object.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
