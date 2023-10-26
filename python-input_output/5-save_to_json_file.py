#!/usr/bin/python3
"""
function that writes an Object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes the representation of my_obj
    to filename.
    Args:
        - my_obj: object to write
        - filename: file to write into
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
