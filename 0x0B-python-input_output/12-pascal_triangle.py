#!/usr/bin/python3
'''Define a Pascal triangle of size n'''


def pascal_triangle(n):
    '''Return a list of lists of integers representing a Pascal
    triangle of size n

    Args:
        n (int): The Pascal triangle\'s size
    '''
    save = [[1]]
    if n <= 0:
        return []
    for i in range(1, n):
        a = save[i-1] + [0]
        b = [0] + save[i-1]
        save.append([a[j] + b[j] for j in range(i+1)])
    return save
