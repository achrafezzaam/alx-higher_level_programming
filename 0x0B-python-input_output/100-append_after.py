#!/usr/bin/python3
'''Define the append_after method'''


def append_after(filename="", search_string="", new_string=""):
    '''Add a line containing new_string after each line
    containing the search_string

    Args:
        filename (str): The path to the file
        search_string (str): The string to look for in each line
        new_string (str): The new string to add
    '''
    with open(filename, "r+", encoding="utf-8") as f:
        w_text = ""
        for line in f:
            w_text += line
            if search_string in line:
                w_text += new_string
        f.seek(0)
        f.write(w_text)
