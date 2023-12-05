#!/usr/bin/python3
"""Module defines an insert file function."""

def append_after(filename="", search_string="", new_string=""):
    """Insert the text after each line that contains a string in file."""
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)

