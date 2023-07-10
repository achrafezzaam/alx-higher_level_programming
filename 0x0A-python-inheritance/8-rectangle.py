#!/usr/bin/python3
'''Define the Rectangle Class which inherits from BaseGeometry'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Create the Rectangle object'''
    def __init__(self, width, height):
        '''Instantiate the Rectangle object

        Args:
            width (int): The rectangle's width
            height (int): the rectangle's height
        '''
        self.__width = width
        self.integer_validator('width', self.__width)
        self.__height = height
        self.integer_validator('height', self.__height)
