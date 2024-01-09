#!/usr/bin/python3
"""Define a class which is MyInt."""


class MyInt(int):
    """Initalize a function that will Invert int operators == and !=."""

    def __eq__(self, value):
        """Return a code that Override == opeaator."""
        return self.real != value

    def __ne__(self, value):
        """Return a code that will Override != operator."""
        return self.real == value
