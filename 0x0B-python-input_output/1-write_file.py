#!/usr/bin/python3
"""Define an Utf object."""


def write_file(filename="", text=""):
    """Return a string to a text file (UTF8)."""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
