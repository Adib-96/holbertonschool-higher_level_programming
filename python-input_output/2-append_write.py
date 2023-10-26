#!/usr/bin/python3
"""
function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    function that append text to the end of a file then returns the number of char added.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        char_count = f.write(text)
    return char_count
