#!/usr/bin/python3
"""

Defines a Square class.

"""

from models.rectangle import Rectangle
"""
...
"""
class Square(Rectangle):
    """
    ...
    """

    def __init__(self, size, x, y, id=None):
        """
        ...
        """
        super().__init__(size,size,x, y, id)
    
    def __str__(self):
        """
        ...
        """
        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(
            self.id, self.x, self.y, self.width
        )