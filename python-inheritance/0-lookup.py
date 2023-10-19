#!/usr/bin/python3

"""Define an object attr lookup function"""


def lookup(obj):
    """Return a list of an object's attributes."""
    return dir(obj)
