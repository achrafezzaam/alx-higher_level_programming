#!/usr/bin/python3
'''Define the inherits_from function'''


def inherits_from(obj, a_class):
    '''Check if obj is inheriting from a_class

    Args:
        obj : The object to check
        a_class: The class to check with
    '''
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
