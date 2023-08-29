#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self._size = size
        self._position = position
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
        
    def my_print(self):
        if self._size == 0:
            print('')
        for i in range(self._size):
            print('#', end="")
            for j in range(self._size - 1):
                print('#', end="")                
            print('')
    @property
    def position(self):
        return self._position
    @position.setter
    def position(self, value):
        if not isinstance(value, (int, int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value