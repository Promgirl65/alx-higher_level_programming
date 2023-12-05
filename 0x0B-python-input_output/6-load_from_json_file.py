#!/usr/bin/python3
"""Module defines JSON read file Function."""



import json

def load_from_json_file(filename):
    """creates Python object from a JSON file"""
    with open(filename) as f:
        return json.load(f)

