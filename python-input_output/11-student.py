#!/usr/bin/python3
"""A student is present"""


class Student(object):
    """Student in class... hehehe"""

    def __init__(self, first_name, last_name, age):
        """Alright, i'm going to call roll"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Jason? PResent!"""
        if attrs is None:
            return self.__dict__
        dictionary = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                dictionary[key] = value
        return dictionary

    def reload_from_json(self, json):
        """Jason is gone!"""
        for key, value in json.items():
            setattr(self, key, value)
