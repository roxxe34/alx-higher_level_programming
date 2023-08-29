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

    def my_print(self):
        """
            Print the square with the character #
        """
        if self.__size == 0:
            print('')
        for i in range(self.__size):
            print('#', end="")
            for j in range(self.__size - 1):
                print('#', end="")
            print('')
