#!/usr/bin/python3
"""The base of the circle??"""
import json


class Base(object):
    """Base Base! No tagging!"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initilizing"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return Json list"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
