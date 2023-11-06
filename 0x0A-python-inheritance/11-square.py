#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent the square."""

    def __init__(self, size):
        """Initialize the new square.

        Args:
            size (int): The size of the new squares.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
