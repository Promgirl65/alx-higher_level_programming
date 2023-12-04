#!/usr/bin/python3
"""
    Module to return list of available attributes and methods of an object
"""

def lookup(obj):
    """Function to check for all attributes and methods of an object"""
    return dir(obj)

