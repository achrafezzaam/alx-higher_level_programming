#!/usr/bin/python3
'''Define the save_to_json_file method'''
import json


def save_to_json_file(my_obj, filename):
    '''Save an object as a Json string in a file

    Args:
        my_obj : The object to save
        filename (str): The file\'s path
    '''
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
