#!/usr/bin/python3
'''Define a Square'''


class Square:
    '''Create a Square object'''
    def __init__(self, size=0):
        '''Instantiate the Square object

        Args:
            size (int): The size of the Square object
        '''
        self.size = size

    @property
    def size(self):
        '''Get the size of the Square object'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Set the new value to the size of the Square object'''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        '''Compute the area of the Square object'''
        return self.__size ** 2
