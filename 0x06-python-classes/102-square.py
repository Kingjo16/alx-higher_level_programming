#!/usr/bin/python3
"""Define a square Class."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """
        Initialize a new sq.

        Args:
            size (int): The size of the sq.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the sq."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the cur sq area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comp based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comp Based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comp based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comp based on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comp based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comp based on area."""
        return self.area() >= other.area()
