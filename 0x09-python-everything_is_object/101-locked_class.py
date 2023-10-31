#!/usr/bin/python3
"""Define the locked class."""


class LockedClass:
    """
    Prevent user from the instantiating new LockedClass attribute
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
