#!/usr/bin/python3
'''Define the add_attribute function'''


def add_attribute(obj, name, value):
    '''Adds a new attribute the given object

    Args:
        obj : The object to add the attribute to
        name (str): The name of the attribute
        value : The value of the attribute
    '''
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
