#!/usr/bin/python3
"""Module that define a function to print a square matrix."""
def print_square(size):
    """Print a square matrix.
    
    Args:
    size (int): size of the square matrix
    Raises:
        TypeError: if size is not integer
        ValueError: if size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
