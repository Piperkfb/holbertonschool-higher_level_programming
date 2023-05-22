#!/usr/bin/python3
"""Print a first and last name: """


def say_my_name(first_name, last_name=""):
    """Print first and last"""

    #must be a string first and last
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")

    #print my name is first last
    print("My name is {:s} {:s}".format(first_name, last_name)
