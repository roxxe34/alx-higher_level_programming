#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a square.

    Attributes:
        size (int): The size of the square.
        x (int): The x-coordinate of the upper-left corner.
        y (int): The y-coordinate of the upper-left corner.
        id (int): The unique identifier.

    Methods:
        update(*args, **kwargs): Update square attributes.
        to_dictionary(): Convert the square to a dictionary.
        __str__(): String representation.

    Inherits from the Rectangle class with 'size' as both width and height.

    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a square.

        Args:
            size (int): The size.
            x (int, optional): The x-coordinate. Defaults to 0.
            y (int, optional): The y-coordinate. Defaults to 0.
            id (int, optional): The identifier. Defaults to None.
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)
        self.size = size

    @property
    def size(self):
        """Get the size."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update square attributes.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        num_args = len(args)

        if num_args == 1:
            self.id = args[0]
        elif num_args >= 2:
            self.id = args[0]
            self.size = args[1]
            if num_args >= 3:
                self.x = args[2]
                if num_args >= 4:
                    self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs['id']
            if "size" in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """
        Convert the square to a dictionary.

        Returns:
            dict: A dictionary representation of the square.
        """
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}

    def __str__(self):
        """String representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
