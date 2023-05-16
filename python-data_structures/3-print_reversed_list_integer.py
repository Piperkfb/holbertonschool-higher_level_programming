#!/usr/bin/python3i
def print_reversed_list_integer(my_list=[]):

    leng = len(my_list)

    while (leng > 0):
        print("{:d}".format(my_list[leng-1]))
        leng -= 1
