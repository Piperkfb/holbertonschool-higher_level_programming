#!/usr/bin/python3
"""Rekt this angle"""


from models.base import Base


class Rectangle(Base):
    """Welcome to Rekt class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """whut"""

        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

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
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for Height"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

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

    @y.setter
    def y(self, y):
        """Setter for Y"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """The area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Shows visual representation of rectangle"""

        for p in range(self.y):
                print("")

        for i in range(self.height):
            for k in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """Displays attributes in a nice way"""
        return ('[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x,
                                                        self.y, self.width,
                                                        self.height))

    def update(self, *args, **kwargs):
        """Update the values"""
        if args != 0:
            a = 0
            for arg in args:
                if a == 0:
                    self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "id":
                    self.id = j
                elif i == "width":
                    self.width = j
                elif i == "height":
                    self.height = j
                elif i == "x":
                    self.x = j
                elif i == "y":
                    self.y = j
