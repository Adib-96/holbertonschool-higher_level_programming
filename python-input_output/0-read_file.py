#!/usr/bin/python3
"""
fucntion that read a text file and print it to stdout
"""

def read_file(filename=""):
    """
    Read file from specified directory
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(),end='')
