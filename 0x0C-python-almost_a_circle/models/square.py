#!/usr/bin/python3
from .rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width =size, height=size, x=x, y=y, id=id)
        self.size = size

    @property
    def size(self):
        return self.width
    @size.setter
    def size(self, value):
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        num_args = len(args)

        # Check the number of arguments passed
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
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"