#!/usr/bin/python3
"""To define a class Square."""


class Square:
    """
    To define a Class square by:(based on 1-square.py).
    """
    def __init__(self, size=0):
        """To initialize square class size.

        Args:
            size: size of square (int).
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
