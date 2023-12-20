#!/usr/bin/python3
"""This defines a square"""


class Square:
    """
    This class also defines a square

    Attributes:
        __size (int): the instance attribue
    """

    def __init__(self, size=0):
        """
        This is an instantiation with option.

        Args:
            size (int, optional): The size of the new square.
        Raises:
            TypeError: size is not an int
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
