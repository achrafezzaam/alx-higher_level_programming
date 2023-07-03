#!/usr/bin/python3
'''Define the print_square method'''


def print_square(size):
    '''Prints a sqaure to stdout

    Args:
        size (int): The size of the printed square
    '''
    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print('#'*size)
