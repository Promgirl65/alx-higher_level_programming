#!/usr/bin/python3
"""This module checks the object instance of a class"""

def is_same_class(obj, a_class):
    """To return True if the object is an instance of the
    class, otherwise False
    """
    return (type(obj) == a_class)
