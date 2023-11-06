#!/usr/bin/python3
"""Define an object attributes lookup function."""


def lookup(obj):
    """Return the list of an object available attribute."""
    return (dir(obj))
