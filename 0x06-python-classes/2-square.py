#!/usr/bin/python3
"""Define a class Square."""


class Square:
    def __init__(self, size=0):
        """initialize a square

        Args:
            size (int): the size of square. Defaults to 0.

        Raises:
            TypeError: raise type error
            ValueError: raise value error
        """
        if not isinstance(size, int):
            raise TypeError("must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
