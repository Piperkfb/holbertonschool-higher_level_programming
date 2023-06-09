#!/usr/bin/python3
"""Pascal is a disney character"""


def pascal_triangle(n):
    """Their triangle"""

    if n <= 0:
        return ""

    triangle = [[1]]
    for cur_row in range(1, n):
        row = [1]
        prev_row = triangle[cur_row - 1]
        for elem in range(1, cur_row):
            row.append(prev_row[elem] + prev_row[elem - 1])
        row.append(1)
        triangle.append(row)
    return (triangle)
