#!/usr/bin/python3
def tuple_to_list(tuple_i=()):
    a = list(tuple_i)
    i = len(a)
    while i < 2:
        a.append(0)
        i += 1
    return a


def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_to_list(tuple_a)
    b = tuple_to_list(tuple_b)
    c = []
    for i in range(2):
        c.append(a[i] + b[i])
    return tuple(c)
