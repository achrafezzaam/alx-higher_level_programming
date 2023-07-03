#!/usr/bin/python3
'''Define the matrix_divided method'''


def matrix_divided(matrix, div):
    '''Divide a mitrix by a given int value

    Args:
        matrix (list(list(int, float))): a list of lists of ints
        and floats
        div (int): The int used to devide the matrix by
    '''
    if (not isinstance(matrix, list) or len(matrix) == 0 or
        not all(isinstance(row, list) and len(row) != 0 for row in matrix) or
        not all((isinstance(i, int) or isinstance(i, float))
                for i in [i for row in matrix for i in row])):
        raise TypeError('matrix must be a matrix '
                        '(list of lists) of integers/floats')
    if len(matrix) > 1:
        for i in range(len(matrix) - 1):
            if len(matrix[i]) != len(matrix[i + 1]):
                raise TypeError('Each row of the matrix '
                                'must have the same size')
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [list(map(lambda new: round(new / div, 2), row)) for row in matrix]
