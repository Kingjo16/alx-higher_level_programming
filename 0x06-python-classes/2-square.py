#!/usr/bin/python3
"""This defines a square"""


class Square:
    """
    This class also defines a square

    Attributes:
        size : instance attribue
    """

    def __init__(self, size=0):
        """
        this is an instantiation with option.
        """
        if type(size) is not int:
             raise TypeError("size must be an integer")
         else:
             if size < 0:
                 raise ValueError("size must be >= 0")
             else:
                 self.__size = size
