#!/usr/bin/python3

"""Define a class(MyList) that inherits from list classe"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""
    def print_sorted(self):
        """Sort a list and print it"""
        print(self.sort())