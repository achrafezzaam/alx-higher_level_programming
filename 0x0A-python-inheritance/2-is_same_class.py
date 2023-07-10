#!/usr/bin/python3
'''Define the is_same_class function'''


def is_same_class(obj, a_class):
    '''Check if obj is the same type as a_class

    Args:
        obj : The object to check
        a_class : The class to check with
    '''
    if type(obj) == a_class:
        return True
    return False
