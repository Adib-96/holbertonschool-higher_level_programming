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
        """Return the width of Rectangle"""
        return self.__width
    
    @property
    def height(self):
        """Return the height of Rectangle"""
        return self.__height
    
    @property
    def x(self):
        """Return the x coordinate of the Rectangle"""
        return self.__x
    
    @property
    def y(self):
        """Return the y coordinate of the Rectangle"""
        return self.__y
    
    @width.setter
    def width(self, value):
        """Set the width value"""
        self.__width = value
    
    @height.setter
    def height(self, value):
        """Set the height value"""
        self.__height = value
    
    @x.setter
    def x(self, value):
        """set the x coordinate of the rectangle"""
        self.__x = value
    
    @y.setter
    def y(self,value):
        """set the y coordinate of the rectangle"""
        self.__y = value
