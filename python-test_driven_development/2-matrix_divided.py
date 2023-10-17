#!/usr/bin/python3
def matrix_divided(matrix, div):
    """"Returns a new matrix which each element will be 
    divided by div variable.
    Args:
        matrix (list) : A list of lists of integers and floats.
        div : a divisor.
    Raises:
        TypeError: 
        {
        - if the matrix contains non numbers.
        - if the matrix contains rows of different sizes.
        - if div is not an int or float
        }
        ZeroDivisionError: if div contains 0.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(e, int) or isinstance(e, float))
                    for e in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    #In summary, this code takes a 2D matrix, 
    #divides each element in the matrix by 4, 
    #and rounds the result to two decimal places. 
    #The result is a new 2D matrix with the same dimensions 
    #as the original, but with updated values.
    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]            