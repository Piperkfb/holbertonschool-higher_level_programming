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
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Display the Square"""
        return ('[Square] ({}) {}/{} - {}'.format(self.id, self.x,
                                                self.y, self.width))
