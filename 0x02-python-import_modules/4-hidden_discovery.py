#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    dir_list = dir(hidden_4)
    for elem in dir_list:
        if elem[:2] != "__":
            print(elem)
