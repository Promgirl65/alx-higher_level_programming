#!/usr/bin/python3
"""This Module defines a class that inherits
from the list class"""

class MyList(list):
    """Class that Inherits from list"""
    def print_sorted(self):
        """prints The sorted list"""
        print(sorted(self))
