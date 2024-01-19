#!/usr/bin/python3
"""Define a rectangle model class."""
from models.base import Base


class Rectangle(Base):
    """Define a rectangle Class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a rectangle instance."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Return Property a width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Write a width value with type erroe and value error."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Return a height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Write a height value with a type and value error."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Return the x coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Write an x value eith typpr and val error."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Return a y coo. val."""
        return self.__y

    @y.setter
    def y(self, value):
        """Write an y value with typr and val error."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return an area with width and height."""
        return self.width * self.height

    def display(self):
        """Define a Display withe a #."""
        new_rec = ""
        printer = "#"

        print("\n" * self.y, end="")

        for m in range(self.height):
            new_rec += (" " * self.x) + (printer*self.width) + "\n"
        print(new_rec, end="")

    def __str__(self):
        """Return a String  with id x and y."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Write an update for args and kwargs."""
        if len(args) == 0:
            for lock, set_val in kwargs.items():
                self.__setattr__(lock, set_val)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """Return a dictionary witha a return of the rect."""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
        }
