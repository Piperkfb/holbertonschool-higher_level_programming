#!/usr/bin/python3
""" Only sub class of"""


def inherits_from(obj, a_class):
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
