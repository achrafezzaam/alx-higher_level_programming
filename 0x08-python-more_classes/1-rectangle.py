#!/usr/bin/python3
'''Define the Rectangle class'''


class Rectangle:
    '''Create a rectangle object'''
    def __init__(self, width=0, height=0):
        '''Instanciate the Rectangle object

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Retrieve the width value'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set a new value to the width

        Args:
            value (int): The new width of the rectangle instance
        '''
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''Retrieve the height value'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set a new value to the height

        Args:
            value (int): The new height of the rectangle instance
        '''
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
