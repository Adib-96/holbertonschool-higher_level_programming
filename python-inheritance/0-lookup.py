#!/usr/bin/python3
"""Module that define a function that return 
the list of available attributes and methods of an object
"""


def lookup(obj):
    """Return the attribute and method of an object
    
    Arguments:
            obj: the object to lookup
    """
    return dir(obj)