#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """
    A class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the upper-left corner.
        y (int): The y-coordinate of the upper-left corner.
        id (int): The unique identifier.

    Methods:
        area(): Calculate the rectangle's area.
        display(): Display the rectangle using '#' characters.
        update(*args, **kwargs): Update rectangle attributes.
        to_dictionary(): Convert the rectangle to a dictionary.
        __str__(): String representation.

    Inherits from the Base class (providing 'id').

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a rectangle.

        Args:
            width (int): The width.
            height (int): The height.
            x (int, optional): The x-coordinate. Defaults to 0.
            y (int, optional): The y-coordinate. Defaults to 0.
            id (int, optional): The identifier. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width.

        Raises:
            TypeError: If not an integer.
            ValueError: If not > 0.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height.

        Raises:
            TypeError: If not an integer.
            ValueError: If not > 0.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate.

        Raises:
            TypeError: If not an integer.
            ValueError: If < 0.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate.

        Raises:
            TypeError: If not an integer.
            ValueError: If < 0.
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the rectangle's area."""
        return self.__width * self.__height

    def display(self):
        """Display the rectangle using '#' characters."""
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
        """
        Update rectangle attributes.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        num_args = len(args)

        if num_args == 1:
            self.id = args[0]
        elif num_args >= 2:
            self.id = args[0]
            self.width = args[1]
            if num_args >= 3:
                self.height = args[2]
                if num_args >= 4:
                    self.x = args[3]
                    if num_args >= 5:
                        self.y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs['id']
            if "width" in kwargs:
                self.width = kwargs['width']
            if "height" in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """
        Convert the rectangle to a dictionary.

        Returns:
            dict: A dictionary representation of the rectangle.
        """
        return {'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width}

    def __str__(self):
        """String representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
