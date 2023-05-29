#!/usr/bin/python3
"""a square is a rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """I am but equal height, equal width"""

    def __init__(self, size):
        """Inilizing init"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """It's a square now"""
        return '[Square] {}/{}'.format(self.__size, self.__size)
