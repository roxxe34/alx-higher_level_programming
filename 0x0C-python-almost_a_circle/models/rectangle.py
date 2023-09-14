#!/usr/bin/python3
from .base import Base
class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <=  0:
            raise ValueError("width must be > 0")
        if value > 0:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val <=  0:
            raise ValueError("height must be > 0")

        self.__height = val

    # Getter and setter methods for x
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    # Getter and setter methods for y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height
    
    def display(self):
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    # Public method to update attributes
    def update(self, *args, **kwargs):
        num_args = len(args)

        # Check the number of arguments passed
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
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height, 'width': self.width}                
    
    def __str__(self):
        return  f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
