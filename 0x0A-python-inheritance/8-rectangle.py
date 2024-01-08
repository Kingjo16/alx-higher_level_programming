#!/usr/bin/python3
"""Define a Rectangle Class inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a BaseGeometry Rectangle."""

    def __init__(self, width, height):
        """Intialize a Rectangle which is new."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
