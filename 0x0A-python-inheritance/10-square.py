#!/usr/bin/python3
"""Module that Defines Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """To Initialize a new square
        Args:
            size (int): size of New square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

