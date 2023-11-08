#!/usr/bin/python3
"""This modules defines a class Student."""


class Student:
    """
    Defines a class Student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Creates Student object instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age: The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary representation of current student."""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of student instance with
        values from a dictionary.

        Args:
            json (dict): A dictionary containing attribute names as
                         keys and their values.
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)        
