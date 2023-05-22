#!/usr/bin/python3
""" Divdes all elemnts of matrix: """


def matrix_divided(matrix, div):
    """Divies the matrix"""

    rowlen = len(matrix)
    collen = len(matrix[0])

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) != int or float:
        raise TypeError("div must be a number")

    for row in matrix:
        if len(row) != collen:
            raise TypeError("Each row of the matrix must have the same size")

    for i in matrix:
        for j in matrix[0]:
            if matrix[i][j] != int or float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                divmat[i][j] = matrix[i][j]/2

    return (divmat)
