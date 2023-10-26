#!/usr/bin/python3
"""
function that writes an Object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file,
    using a JSON representation.
    :param my_obj: Object to be added to the file
    :param filename: name of a file
    :return: none
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
