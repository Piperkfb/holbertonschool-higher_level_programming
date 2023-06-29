#!/usr/bin/python3
"""Prints a square: """


def print_square(size):
    """Prints a square"""

    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise TypeError("size must be >= 0")

    for j in range(size):
        for i in range(size):
            print("#", end="")
        print("")
