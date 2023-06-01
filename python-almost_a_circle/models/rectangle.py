#!/usr/bin/python3
"""Rekt this angle"""


from models.base import Base


class Rectangle(Base):
    """Welcome to Rekt class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """whut"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for Width"""
        self.__width = width

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for Height"""
        self.__height = height

    @property
    def x(self):
        """Getter for X"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for X"""
        self.__x = x

    @property
    def y(self):
        """Getter for Y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for Y"""
        self.__y = y
