#!/usr/bin/python3

"""This Defines a class Square."""


class Square:
    """This represents a square which is new."""

    def __init__(self, size):
        """Int a new square that is new.

        Args:
            size(int): the siz of the square.
        """
        self.size = size

    @property
    def size(self):
        """It set a new size to a current sie of sq."""
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
        """Return the area of the sq."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print a square using the has char."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
