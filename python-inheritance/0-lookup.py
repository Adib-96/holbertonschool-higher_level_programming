#!/usr/bin/python3

def lookup(obj):
    """
    Get the list of available attributes and methods of an object.
    
    Args:
        obj: Any Python object.
        
    Returns:
        List containing attributes and methods of the object.
    """
    return dir(obj)
