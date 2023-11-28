#!/usr/bin/python3
"""

This module contains the Function that adds 2 integers

"""


def add_integer(a, b=98):
    """This returns Sum of the numbers: integers or floats

    Args:
        a: argument one
        b: argument two

    Returns:
        The Sum of the 2 arguments

    Raises:
        TypeError: If any of the arguments is not integer or float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

