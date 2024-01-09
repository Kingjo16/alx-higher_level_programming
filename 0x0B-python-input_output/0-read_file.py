#!/usr/bin/python3
"""Define file-reading fun."""


def read_file(filename=""):
    """Read the text file(content) of UTF8 text file to stdout."""
    with open(filename, 'r', encoding='utf-8') as f:
        print(file.read(), end="")
