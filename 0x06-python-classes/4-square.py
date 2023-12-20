#!/usr/bin/python3
"""THis define a square"""


class Square:
    """
    represrnts a square.

    Attributes:
        __size (int): The size of the sq.
    """

    def __init__(self, size=0):
        """
        intialize a new sq class.
        Args:
            size (int, optional): The size of the sq.
        Raises:
            TypeError: If size is not an int.
            ValueError: If size is less than 0.
        """
        self.size = size

    def area(self):
        """
        clac the area.

        Return:
            int: The area of the square.
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """
        the size attribute.

        Returns:
            int: the size of the sq.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter meth for the si att.

        Args:
            value (int): the size set
        Raises:
            TypeError: Value not an int.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
