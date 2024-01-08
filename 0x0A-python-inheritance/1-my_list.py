#!/usr/bin/python3
"""A class which is My list."""


class MyList(list):
    """List sub class."""

    def __init__(self):
        """Initialize the object."""
        super().__init__()

    def print_sorted(self):
        """Print a list whhcih is sorted list."""
        print(sorted(self))
