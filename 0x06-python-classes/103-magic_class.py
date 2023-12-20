#!/usr/bin/python3
"""Defines a MagicClass with bytcodes."""

import math


class MagicClass:
    """Defines the MagicClass with circule."""

    def __init__(self, radius=0):
        """Initialize the MagicClass instance.

        Args:
            radius (int or float, optional): The radius of the circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference of the circle."""
        return 2 * math.pi * self.__radius
