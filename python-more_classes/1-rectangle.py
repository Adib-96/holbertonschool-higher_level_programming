#!/usr/bin/python3
"""

Module with a Rectangle class

"""


class Rectangle:
    """

    A class to represent a Rectangle

    """
    def __init__(self, width=0, height=0):
        """

        Checks the parameters and initializes some values

        Args:
            width (:obj:`int`, optional): The width of the Rectangle.
            height (:obj:`int`, optional): The height of the Rectangle.

        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        
        Return the width of the Rectangle
        
        """
        return self.__width

    @width.setter
    def width(self, value):
        """

        Checks the parameters and set the size of the Rectangle

        Args:
            value (int): The width of the Rectangle.

        Raises:
            TypeError: If `value` type is not `int`.
            ValueError: If `value` is less than `0`.

        """
        if type(value) is int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """

        Return the height of the rectangle.
        
        """
        return self.__height

    @height.setter
    def height(self, value):
        """

        Checks the parameters and set the size of the Rectangle

        Args:
            value (int): The height of the Rectangle.

        Raises:
            TypeError: If `value` type is not `int`.
            ValueError: If `value` is less than `0`.

        """
        if type(value) is int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
