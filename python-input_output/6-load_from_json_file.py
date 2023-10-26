#!/usr/bin/python3
"""
 function that creates an Object from a “JSON file
"""
import json


def load_from_json_file(filename):
    """
    function that writes an Object to a text file, using a JSON representation
    """
    return json.loads(filename)
