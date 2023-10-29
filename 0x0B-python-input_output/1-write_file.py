#!/usr/bin/python3
"""Module Defines the Write_file function"""

def write_file(filename="", text=""):
    """Writes String to UTF8 text file."""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
