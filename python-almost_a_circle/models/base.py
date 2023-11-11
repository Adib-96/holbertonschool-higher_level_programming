#!/usr/bin/python3
"""
Module with a Base class
"""

import json

class Base:
    """
    Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new instance of the Base class
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        ...
        """
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return "[]"
        
        return json.dumps(list_dictionaries)
