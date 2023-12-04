#!/usr/bin/python3
"""Function that add attributes to objects"""

def add_attribute(obj, att, value):
    """Adds new attribute to object if Possible"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

