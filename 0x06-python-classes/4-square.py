#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self._size = size
    def area(self):
        return self._size * self._size
    
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value
        
