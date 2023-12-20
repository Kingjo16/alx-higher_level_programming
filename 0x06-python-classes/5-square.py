#!/usr/bin/python3
"""This Defines a class Square."""


class Square:
    """this represents a square which is new."""

    def __init__(self, size):
        """int a new square that is new.

        Args:
            sixe(int): the siz of the square.
        """
        self.size = size

    @property
    def size(self):
        """it set a new size to a current sie of sq."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size to set.
        Raises:
            TypeError: Value is not an int
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This Return the area of the sq"""
        return (self.__size * self.__size)

    def my_print(self):
        """PRints a square using the has char."""
        if self.__size == 0:
            print("")
        else:
            for m int range(self.__size):
                print("#"*self.__size)
