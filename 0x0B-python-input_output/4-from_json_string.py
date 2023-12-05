#!/usr/bin/python3
"""define JSON-to-object function."""

import json

def from_json_string(my_str):
    """returns Python object representation Of a JSON String"""
    return json.loads(my_str)

