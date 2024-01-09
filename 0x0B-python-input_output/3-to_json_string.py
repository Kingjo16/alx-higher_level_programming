#!/usr/bin/python3
"""Define a JSON function changer."""
import json


def to_json_string(my_obj):
    """Return the (JSON) representation obj."""
    return json.dumps(my_obj)
