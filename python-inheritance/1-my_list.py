#!/usr/bin/python3
"""A child is born"""


class Mylist(list):
    """It will inherit and print."""

    def print_sorted(self):
        """As says"""
        print(sorted(self))
