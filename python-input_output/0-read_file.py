#!/usr/bin/python3
def read_file(filename=""):
    """Read file from specified directory"""
    with open(filename, 'r', encoding="UTF8") as f:
        return f.read()
