#!/usr/bin/python3
"""
function that write a string to a text file
"""


def write_file(filename="", text=""):
    """
    write string to a text file and return the number of charcter written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        char_count = f.write(text)
    return char_count
