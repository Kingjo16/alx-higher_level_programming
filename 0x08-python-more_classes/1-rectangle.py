#!/usr/bin/python3
"""Define a Rectangle Class."""


class Rectangle:
    """Define a rectangle with width and height instanec."""

    def __init__(self, height=0, width=0):
        """Initialize the rectangle with hight and width to 0."""
        self.height = width
        self.width = height

    @property
    def height(self):
        """Return a height method."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for hight."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """Return a width method."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
