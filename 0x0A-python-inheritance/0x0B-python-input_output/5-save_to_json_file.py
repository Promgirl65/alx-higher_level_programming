#!/usr/bin/python3
"""defines JSON file-writing function.."""


import json

def save_to_json_file(my_obj, filename):
    """Writes object to Text file in JSON format"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
