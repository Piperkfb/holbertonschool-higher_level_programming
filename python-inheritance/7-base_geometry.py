#!/usr/bin/python3
"""You think I'm not documenting?"""


class BaseGeometry(object):
    """Empty Students"""

    def area(self):
        """return area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) =! int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be an integer".format(name))
