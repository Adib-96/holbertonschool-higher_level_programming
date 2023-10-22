#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    def area(self):
        """Not yet implemented"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Validate a paramaetre as an integer.
        
        Args:
            name (str): name of parametre.
            value (int): parameter to validate.
        Raises:
        TypeError: if value is not an integer.
        ValueError: if value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        