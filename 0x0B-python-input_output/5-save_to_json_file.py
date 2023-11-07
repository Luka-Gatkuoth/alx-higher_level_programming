#!/usr/bin/python3
"""Define the JSON file-writing functions."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to the text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
