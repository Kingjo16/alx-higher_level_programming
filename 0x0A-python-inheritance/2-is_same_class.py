#!/usr/bin/python3
"""Define a function which will check a class."""


def is_same_class(obj, a_class):
    """Check if an object is an onstance class or not."""
    if type(obj) is a_class:
        return True
    return False
