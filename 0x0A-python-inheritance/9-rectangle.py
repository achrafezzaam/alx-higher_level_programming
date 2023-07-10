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

    def area(self):
        '''Return the area of the Rectangle object'''
        return self.__width * self.__height

    def __repr__(self):
        '''Define the print output'''
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__width, self.__height)

    def __str__(self):
        '''Define the message printed at object creation'''
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__width, self.__height)
