#!/usr/bin/python3
"""

Modules that define a Square class

"""


class Square:
    """

    Represent a new square

    """
    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int) : The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """get/set the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """get/set the size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the current area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
