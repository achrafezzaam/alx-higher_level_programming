#!/usr/bin/python3
'''Define the BaseGeometry class'''


class BaseGeometry:
    '''Create the BaseGeometry object'''
    def area(self):
        '''Raise an exception error when called'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Check if value is strictly greater than 0'''
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
