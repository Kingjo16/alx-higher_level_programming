#!/usr/bin/python3
"""Defin a class which is student-class."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student function."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary rep of a student."""
        return self.__dict__
