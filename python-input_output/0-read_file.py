#!/usr/bin/python3
"""

Module that create a function that read file and return

"""


def read_file(filename=""):
    """Read file from specified directory"""
    with open(filename, 'r') as f:
        return f.read()
