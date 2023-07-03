#!/usr/bin/python3
'''Define the text_indentation method'''


def text_indentation(text):
    '''Split a string by the characters [., ?, :] then prints
    each sentence to stdout followed by two new lines.

    Args:
        text (str): The string to be formated
    '''
    if type(text) != str:
        raise TypeError('text must be a string')
    save = ''
    for i in range(len(text)):
        if text[i] in [".", "?", ":"]:
            save += text[i]
            print(save.strip(), end="\n\n")
            save = ''
        else:
            save += text[i]
    print(save.strip(), end="")
