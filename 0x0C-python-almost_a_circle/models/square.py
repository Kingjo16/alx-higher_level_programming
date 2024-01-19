#!/usr/bin/python3
"""Define a square class model."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square that implement from a rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Define initalize a square with id y x and size set."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return a size with a given width."""
        return self.width

    @size.setter
    def size(self, value):
        """Write a size with a value typr and val error."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Define an update args and kwargs."""
        if len(args) == 0:
            for lock, set_val in kwargs.items():
                self.__setattr__(lock, set_val)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        """Return a dictionary with id x and size."""
        return {
            "id": self.id,
            "x": self.x,
            "size": self.width,
            "y": self.y
        }

    def __str__(self):
        """Return a square value with the given stance."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
