#!/usr/bin/python3
"""Define an inherited a fun which will check a class."""


def inherits_from(obj, a_class):
    """Check if an obj is a sub class."""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
