#!/usr/bin/python3
"""Define Appending fun."""


def append_write(filename="", text=""):
    """Return a string to the end of a UTF8 text file."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
