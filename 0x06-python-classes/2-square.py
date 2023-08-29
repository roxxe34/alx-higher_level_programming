#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """
    A class representing a square.
    """
    def __init__(self, size=0):
        """initialize a square

        Args:
            size (int): the size of square. Defaults to 0.

        Raises:
            TypeError: raise type error
            ValueError: raise value error
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
