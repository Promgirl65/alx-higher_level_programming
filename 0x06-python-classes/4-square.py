#!/usr/bin/python3
"""To write a class that defines a square."""


class Square:
    """Represents the square class."""

    def __init__(self, size=0):
        """Initializing the square class
        Args:
            size: Size of square (int).
        Raises:
            TypeError: if size is not an integer.
            ValueError: if size < 0
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """To get the size of the Square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        To calculate the square class Area.
        Returns: The new Square Area.
        """

        return (self.__size ** 2)
