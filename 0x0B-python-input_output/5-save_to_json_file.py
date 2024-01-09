#!/usr/bin/python3
"""Defines a JSON function Object."""
import json


def save_to_json_file(my_obj, filename):
    """Write with a JSON representation object."""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
