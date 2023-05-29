#!/usr/bin/python3
"""A rectangle is a square but a square is not a rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """I am but equal height, equal width"""

    def __init__(self, size):
        """Inilizing init"""
        self.integer_validation("size", size)
        self.__size = size

    def area(self):
        """Square as can be"""
        return self.__size * self.__size
