#!/usr/bin/python3
"""To define a square class."""


class Square:
    """Represents the square."""

    def __init__(self, size=0):
        """Initializing the square class size.
        Args:
            size: size of square.
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
        """To get the size of the square."""

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
        To Calculate the square Area.
        Returns: The new Square Area.
        """

        return (self.__size ** 2)

    def my_print(self):
        """To Print the square in # """

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
