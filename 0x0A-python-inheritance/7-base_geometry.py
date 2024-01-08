#!/usr/bin/python3
"""Define a class of BaseGeometry."""


class BaseGeometry:
    """Reprsent a Geometry Base."""

    def area(self):
        """Area implementer and befor implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Define is a validator parameter as an integer."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
