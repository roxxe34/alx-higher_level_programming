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
        """
        self.__size = size

    def area(self):
        """the current square area

        Returns:
            (int): returns the current square area
        """
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of the square

        Args:
            value (int): the new size of the square

        Raises:
            TypeError: raised when the size is not integer
            ValueError: rasied when the size is not positive
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
