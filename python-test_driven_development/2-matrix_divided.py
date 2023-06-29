#!/usr/bin/python3
""" Divdes all elemnts of matrix: """


def matrix_divided(matrix, div):
    """Divies the matrix"""

    rowlen = len(matrix)
    collen = len(matrix[0])

    if rowlen == 0 or collen == 0:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if not all(len(row) == len(matrix[0]) for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        for element in row:
            if type(element) != int and float:
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")

    return [[round(element/div, 2) for element in row] for row in matrix]
