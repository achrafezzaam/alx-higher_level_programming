#!/usr/bin/python3
'''Define the BaseGeometry class'''


class BaseGeometry:
    '''Create the BaseGeometry object'''
    def area(self):
        '''Raise an exception error when called'''
        raise Exception('area() is not implemented')
