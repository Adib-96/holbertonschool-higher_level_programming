#!/usr/bin/python3
"""
Function that handles JSON representation
"""
import json


def from_json_string(my_str):
    """function that convert JSON to Python ;)"""
    return json.loads(my_str)
