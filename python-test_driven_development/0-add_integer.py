#!/usr/bin/python3
"""Adds two integers: """


def add_integer(a, b=98):
    """adds two inegers"""
    if (a is None or a is not isinstance(a, int) and a is not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (b is not isinstance(b, int) and b is not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
