#!/usr/bin/python3
"""Define a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a rectangle square."""

    def __init__(self, size):
        """Initialize a square with size size."""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
