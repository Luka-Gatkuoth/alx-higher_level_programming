#!/usr/bin/python3
"""Define the class-checking functions."""


def is_same_class(obj, a_class):
    """Checks if an object is exactly the instance of the given class.

    Args:
        obj (any): The object to be check.
        a_class (type): The class to match the type of object to.
    Returns:
        If object is exactly the instance of the class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
