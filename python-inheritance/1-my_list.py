#!/usr/bin/python3
"""A child is born"""


class MyList(list):
    """It will inherit and print."""

    def print_sorted(self):

        print(sorted(self))
