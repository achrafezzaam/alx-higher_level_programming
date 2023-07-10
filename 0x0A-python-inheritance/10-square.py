#!/usr/bin/python3
'''Define the Square class which inherits from Rectangle'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Create the Square object'''
    def __init__(self, size):
        '''Instantiate the Square object

        Args:
            size (int): the size of the square'''
        self.__size = size
        self.integer_validator('size', self.__size)
        super().__init__(size, size)
