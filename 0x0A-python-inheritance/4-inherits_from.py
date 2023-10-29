#!/usr/bin/python3
"""Module Checks if object is instance of a class that is
inherited from a specified class
"""


def inherits_from(obj, a_class):
    """returns True if object is an instance of the inherited class, 
    otherwise False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
