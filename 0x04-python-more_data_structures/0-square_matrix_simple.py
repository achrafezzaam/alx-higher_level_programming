#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    ans = []
    for elem in matrix:
        ans.append(list(map(lambda x: x**2, elem)))
    return ans
