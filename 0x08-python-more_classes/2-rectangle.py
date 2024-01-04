#!/usr/bin/python3
"""Define a classs which defines a rectangele."""


class Rectangle:
    """Define a rectangle by : based on 1-rectangle.py."""

    def __init__(self, width=0, height=0):
        """Initialize the rectange with widt nd height with 0."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return a width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sette for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Return height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return and cal. the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__width + self.__height)
