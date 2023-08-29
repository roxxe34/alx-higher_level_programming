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
        self.size = size
        self.position = position

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
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """the current square area

        Returns:
            (int): returns the current square area
        """
        return self.__size ** 2

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
