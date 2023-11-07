#!/usr/bin/python3
"""Define the strings to JSON functions."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of the string object."""
    return json.dumps(my_obj)
