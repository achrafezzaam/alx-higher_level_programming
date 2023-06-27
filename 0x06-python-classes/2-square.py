#!/usr/bin/python3
'''Define a Square'''


class Square:
    '''Create a Square object'''
    def __init__(self, size=0):
        '''Instantiate the Square object

        Args:
            size (int): The size of the Square object
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
