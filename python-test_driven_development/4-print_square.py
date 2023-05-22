#!/usr/bin/python3
"""Prints a square: """


def print_square(size):
    """Prints a square"""

    if size < 0:
        raise TypeError("size must be >= 0")

    if type(size) != int:
        raise TypeError("size must be an integer")

    for j in range(size):
        for i in range(size):
            print("#", end="")
        print("")
