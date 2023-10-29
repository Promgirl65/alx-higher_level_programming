#!/usr/bin/python3
"""defines a class Student."""

class Student:
    """represents the Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self):
        """gets dictionary Representation ofStudent"""
        return self.__dict__
