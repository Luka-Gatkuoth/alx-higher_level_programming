#!/usr/bin/python3
"""Define the  Python class-to-JSON functions."""


def class_to_json(obj):
    """Return the dictionary represntation of the simple data structure."""
    return obj.__dict__
