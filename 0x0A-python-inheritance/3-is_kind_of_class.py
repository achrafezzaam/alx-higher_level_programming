#!/usr/bin/python3
'''Define the is_kind_of_class function'''


def is_kind_of_class(obj, a_class):
    '''Check if object is an instance of a_class

    Args:
        obj : The object to check
        a_class: The class to check with
    '''
    return isinstance(obj, a_class)
