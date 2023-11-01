#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Intialize a new Rectangle object.
        
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
    
    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width
    
    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height
    
    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x
    
    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y
    
    @width.setter
    def width(self, value):
        self.__width = value
    
    @height.setter
    def height(self, value):
        self.__height = value
    
    @x.setter
    def x(self, value):
        self.__x = value
    
    @y.setter
    def y(self,value):
        self.__y = value
