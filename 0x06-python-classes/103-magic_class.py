#!/usr/bin/python3
'''Define the MagicClass class'''
import math


class MagicClass:
    '''Create the MagicClass object'''
    def __init__(self, radius=0):
        '''Instantiate the MagicClass object

        Args:
            radius (int or float): The radius of the Disk
        '''
        self.__radius = 0
        if (type(radius) is not int and type(radius) is not float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        '''Computes the area of the Disk'''
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        '''Computes the circumference of the Disk'''
        return (2 * math.py * self.__radius)
