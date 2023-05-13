#!/usr/bin/python3
for first in range(10):
    for last in range(first + 1, 10):
        if first == 8 and last == 9:
            print(f"{first}{last}")
        else:
            print(f"{first}{last}, ", end="")
