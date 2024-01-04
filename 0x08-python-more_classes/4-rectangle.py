#!/usr/bin/python3
"""Define a clas for rectangle."""


class Rectangle:
    """Define a rectangle for 2-rectangle.py."""

    def __init__(self, width=0, height=0):
        """Initialize a width and height of the rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return a wisth method."""
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

    @property
    def height(self):
        """Return the height Method."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Represent a string of the rectangle will be returned."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rep = []
        for m in range(self.__height):
            [rep.append('#') for j in range(self.__width)]
            if m != self.__height - 1:
                rep.append("\n")
        return ("".join(rep))

    def __repr__(self):
        """Return the string rep of the rec."""
        rep = "Rectangle(" + str(self.__width)
        rep += ", " + str(self.__height) + ")"
        return rep
