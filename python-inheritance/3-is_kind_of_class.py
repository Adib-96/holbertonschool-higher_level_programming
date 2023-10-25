#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checks if `obj` is an instance of `a_class`
    
    Args:
        obj (any):The object to compare
        a_class (any):The class to compare with the object
    Returns:
        returns `True` if the object is an instance of, 
        or if the object is an instance of a class that inherited from, 
        the specified class ; otherwise `False`.
    """
    if isinstance(obj, a_class):
        return True
    return False
