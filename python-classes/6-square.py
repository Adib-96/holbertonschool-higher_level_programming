#!/usr/bin/python3
"""

Modules that define a Square class

"""


class Square:
    """

    Represent a new square

    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int) : The size of the square.
            position (int , int) : The position of the new square.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Get/Set the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Get/Set the position of the square"""

        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square"""
        return (self.__size ** self.__size)

    def my_print(self):
        """
        print a square from the size using #

        Returns:
            None
        """
        if self.size == 0:
            print()
        else:
            print('\n'*self.__position[1], end='')
            for i in range(0, self.__size):
                print(' '*self.__position[0], end='')
                print('#'*self.__size)

