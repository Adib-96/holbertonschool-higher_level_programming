#!/usr/bin/python3
"""Module with a Base class."""


class Base:
    """Represent the base model.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """
    
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
