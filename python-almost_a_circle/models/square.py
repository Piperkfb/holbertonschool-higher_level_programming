#!/usr/bin/python3
""" Square"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """Welcome to square class. no B*tches"""

    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, size):
        """setter for size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be > 0")
        self.__size = size

    @property
    def x(self):
        """Getter for X"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for X"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Getter for Y"""
        return self.__y

    @y.setter(self, y):
        """Setter for Y"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
