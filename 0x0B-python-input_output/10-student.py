#!/usr/bin/python3
"""Define a student with a class_Student."""


class Student:
    """Represent a student Class."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student with new things."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary represen of the Student."""
        if attrs is not None and all(isinstance(ele, str) for ele in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
