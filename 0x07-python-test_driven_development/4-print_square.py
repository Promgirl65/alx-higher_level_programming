#!/usr/bin/python3
"""Function that prints a square.

Attributes:
    print_square: Function that prints a square.
"""


def print_square(size):
    """Function that prints a square with the character #.

    Args:
        size (int): Size of the square length.

    Raises:
        TypeError: If Size is not integer.
        ValueError: If size is < 0.
    """
    message = "size must be an integer"

    if not isinstance(size, int):
        raise TypeError(message)

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError(message)

    for i in range(size):
        print("#" * size)
