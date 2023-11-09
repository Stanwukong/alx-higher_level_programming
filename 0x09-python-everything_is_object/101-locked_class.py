#!/usr/bin/python3
"""Defines a LockedClass."""


class LockedClass:
    """
    Allows only first_name as attribute.
    """
    __slots__ = ["first_name"]
