#!/usr/bin/python3

"""Module that defines the square """


class Square:
    """A class that represents the square"""

    def __init__(self, size=0):
        """Initializing the square class
        Args:
            size: represnets the size of square defined
        Raises:
            TypeError: if size is not integers
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Calculate area of the squares
        Returns: The square of size
        """

        return (self.__size ** 2)
