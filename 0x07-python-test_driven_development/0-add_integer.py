#!/usr/bin/python3
'''Define the add_integer method'''


def add_integer(a, b=98):
    '''Return the sum of two given numbers'''
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    else:
        a = int(a)
        b = int(b)
        return a + b
