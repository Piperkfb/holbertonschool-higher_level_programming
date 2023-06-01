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
