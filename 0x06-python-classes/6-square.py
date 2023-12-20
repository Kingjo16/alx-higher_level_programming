#!/usr/bin/python3

"""It defines a class Square."""

class Square:
    """
    Represents a square.

    Attributes:
        size (int): Size of sq
        position (tuple): postition of the sq.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Print a new sq.

        Args:
            size (int): Size of sq
            position (tuple): postition of the sq.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Get or set size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get or set the po of the size."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the sq. using the # chr."""
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
