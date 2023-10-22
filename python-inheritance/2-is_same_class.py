#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Checks if `obj` is exactly an instance of `a_class`
    
    Args:
    obj(any):The object to compare
    a_class(any):The class to compare with the object

    Returns:
    `True` if `obj` is exactly an instance of `a_class` 
     otherwise returns `False
    """
    if type(obj) == a_class:
        return True
    return False