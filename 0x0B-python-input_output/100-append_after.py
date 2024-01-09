#!/usr/bin/python3
"""Define a text file insertion function 100-append_after."""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line text after each Line"""
    texts = ""
    with open(filename) as f:
        for line in f:
            texts += line
            if search_string in line:
                texts += new_string
    with open(filename, "w") as w:
        w.write(text)
