#!/usr/bin/python3
"""Define a JSON function changer."""
import json


def from_json_string(my_str):
    """Return the (JSON) representation obj for python obj."""
    return json.loads(my_str)
