#!/usr/bin/python3
"""Defines the class MyInt that inherit from int"""

class MyInt(int):
    """Defines the Class Myint"""
    def __eq__(self, other):
        return int(str(self)) != other

    def __ne__(self, other):
        return int(str(self)) == other
