#!/usr/bin/python3

def read_file(filename=""):
    """Read file from specified directory"""
    with open(filename, 'r') as f:
        f.read()
