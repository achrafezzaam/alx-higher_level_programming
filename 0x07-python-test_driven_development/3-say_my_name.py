#!/usr/bin/python3
'''Define the say_my_name method'''


def say_my_name(first_name, last_name=""):
    '''Print the message My name is first_name last_name

    Args:
        first_name (str): The first name value
        last_name (str): The last name value
    '''
    if not type(first_name) is str:
        raise TypeError('first_name must be a string')
    if not type(last_name) is str:
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
