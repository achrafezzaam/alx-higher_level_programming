#!/usr/bin/python3
'''Define the from_json_string method'''
import json


def from_json_string(my_str):
    '''Create an object from a json string

    Args:
        my_str (str): The json string to turn into an object'''
    return json.loads(my_str)
