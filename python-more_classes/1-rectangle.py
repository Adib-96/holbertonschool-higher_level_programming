#!/usr/bin/python3
"""

Module with a Rectangle class

"""


class Rectangle:
    """

    A class to represent a Rectangle

    ...

    Attributes
    ----------
    width : int
        width of a Rectangle
    height : int
        height of a rectangle

    Methods
    -------






    """
    def __init__(self, width=0, height=0):
        """

        Constructs all the necessary attributes for the Rectangle object.

        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Return the width attr"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Return the height attr"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value