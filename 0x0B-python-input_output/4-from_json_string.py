#!/usr/bin/python3
# 6-from_json_string.py
"""Define the JSON to object functions."""
import json


def from_json_string(my_str):
    """Return the Python object representation of the JSON strings."""
    return json.loads(my_str)
