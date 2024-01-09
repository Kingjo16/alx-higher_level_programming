#!/usr/bin/python3
"""Define a JSON function object."""
import json


def load_from_json_file(filename):
    """Write a Python object from a JSON file that is present."""
    with open(filename) as f:
        return json.load(f)
