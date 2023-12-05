#!/usr/bin/python3
"""Module defines Python class-to-JSON function.."""

def class_to_json(obj):
    """return the dictionary representation of simple data structure."""
    return obj.__dict__

