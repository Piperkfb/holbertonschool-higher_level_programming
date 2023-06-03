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
    def update(self, *args, **kwargs):
        """Update what you want"""
        if args and args != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        super().__init__(self.width,
                                            self.height, self.x,
                                            self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "id":
                    if i is None:
                        super().__init__(self.width, self.height,
                                            self.x, self.y)
                    else:
                        self.id = j
                elif i == "size":
                    self.size = j
                elif i == "x":
                    self.x = j
                elif i == "y":
                    self.y = j

    def is_dictionary(self):
