#!/usr/bin/python3
"""Define an object add attributer."""


def add_attribute(obj, att, value):
    """Add an object att and val."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
