#!/usr/bin/python3
"""ShapSha:  """


class Rectangle(object):
    """Define new class"""
    def __init__(self, width=0, height=0):
        """Initialize new class rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set values to width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Hight attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set values to height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Define area"""
        return self.__width * self.__height

    def perimeter(self):
        """define perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """ String reresentation of square """
        string = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        x = "#" * self.width
        rect = x
        for i in range(self.height - 1):
            rect += "\n" + x
        return rect

    def __repr__(self)
    """String rep of rec"""
    return "Rectangle({}, {})".format(str(self.width), str(self.height))
