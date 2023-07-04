#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number

    Args:
        matrix (list): The matrix represented as a list of lists
        div (int or float): The number to divide the matrix elements by

    Returns:
        list: The new matrix with the elements divided by div

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats
        TypeError: If each row of the matrix does not have the same size
        TypeError: If div is not a number (integer or float)
        ZeroDivisionError: If div is equal to 0
    """
    if not isinstance(matrix, list) \
            or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return (new_matrix)
