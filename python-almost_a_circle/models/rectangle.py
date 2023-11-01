#!/usr/bin/python3
"""
the class Rectangle that inherits from Base
"""
from models import Base



class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Construct a Rectangle object"""
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
