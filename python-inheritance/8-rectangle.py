#!/usr/bin/python3
"""The rectangle problem"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Geometric Base"""

    def __init__(self, width, height):
        """Initilizing the Rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height". height)
        self.__height = height
