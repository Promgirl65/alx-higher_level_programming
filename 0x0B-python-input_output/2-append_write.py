#!/usr/bin/python3
"""module defines function to append file"""

def append_write(filename="", text=""):
    """append_write string at the end of UTF-8 text file."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

