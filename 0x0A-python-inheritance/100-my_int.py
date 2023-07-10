#!/usr/bin/python3
'''Define the MyInt class'''


class MyInt(int):
    '''MyInt inherits from int and rewrites the == and != methods'''
    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
