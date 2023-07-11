#!/usr/bin/python3
'''Add all the arguments to a Python list then saves them
in the file add_item.json'''
from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    arg_list = load_from_json_file("add_item.json")
except Exception as e:
    arg_list = []
for elem in argv[1:]:
    arg_list.append(elem)

save_to_json_file(arg_list, "add_item.json")
