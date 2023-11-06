#!/usr/bin/python3
"""Define the function that add attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an objects if possible.

    Args:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add to obj.
        value (any): The value of attri.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
