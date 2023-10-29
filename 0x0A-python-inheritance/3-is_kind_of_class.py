#!/usr/bin/python3
"""Module to check if object is the instance of class
or inherited class"""

def is_kind_of_class(obj, a_class):
    """Returns True if object is instance of class
    or the class inherited
    """
    return (isinstance(obj, a_class))
