#!/usr/bin/python3
"""A student is present"""


class Student(object):
    """Student in class... hehehe"""

    def __init__(self, first_name, last_name, age):
        """Alright, i'm going to call roll"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Jason? PResent!"""
        return self.__dict__
