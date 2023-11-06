#!/usr/bin/python3
"""Define the inherited lists class MyList."""


class MyList(list):
    """Implement sorted printing, for built-in list class."""

    def print_sorted(self):
        """Print the list in sorted ascending order."""
        print(sorted(self))
