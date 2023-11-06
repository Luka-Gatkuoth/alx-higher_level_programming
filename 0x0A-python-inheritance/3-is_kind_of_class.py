#!/usr/bin/python3
"""Define the class and inherited class-checking functions."""


def is_kind_of_class(obj, a_class):
    """Check if the object is an instance or inherited instance of the class.

    Args:
        obj (any): The object to be check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
