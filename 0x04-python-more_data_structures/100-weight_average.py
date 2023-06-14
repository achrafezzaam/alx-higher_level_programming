#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_sc = 0
    sum_w = 0
    if my_list is not None and len(my_list) > 0:
        for elem in my_list:
            sum_sc += elem[0] * elem[1]
            sum_w += elem[1]
        return sum_sc / sum_w
    return 0
