#!/usr/bin/python3
"""

Defines a Matrix Division Function

"""


def matrix_divided(matrix, div):
    """Function divides all elements of a Matrix by given number

    Args:
        matrix: A list of lists (matrix)- can be integers or floats
        div: Value to be used for the division (float or integer)
    Raises:
        TypeError: If the matrix contains a list of non-numbers
        TypeError: If the matrix contains rows nothaving same size
        TypeError: If div is not an integer or float
        ZeroDivisionError: If div equals to 0

    Returns:
        A new matrix which is the result of the divisions
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
