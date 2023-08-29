#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """
    A class representing a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """initialize a square

        Args:
            size (int): the size of square. Defaults to 0.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of the square

        Args:
            value (int): value to set the position

        Raises:
            TypeError: raised when the tuple have no integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("Position must be a tuple of 2 positive integers")
        if not all(isinstance(val, int) and val > 0 for val in value):
            raise TypeError("Position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
