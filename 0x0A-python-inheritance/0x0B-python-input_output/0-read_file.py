#!/usr/bin/python3
"""This module contains file-reading function"""

def read_file(filename=""):
    """read file and Print the contents of text file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
