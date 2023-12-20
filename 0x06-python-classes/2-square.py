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
        This is an instantiation with option.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
