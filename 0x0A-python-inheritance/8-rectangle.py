#!/usr/bin/python3
"""Define the class Rectangle that inherits from the BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent the rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize the new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
