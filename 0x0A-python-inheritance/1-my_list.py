#!/usr/bin/python3
"""This module demonstrates class inheritance."""


class MyList(list):
    """Provides additional functionality for list."""

    def print_sorted(self):
        """Prints list in ascending order."""

        sorted_list = sorted(self)
        print(sorted_list)
