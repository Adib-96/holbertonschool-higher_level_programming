#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    num = 0
    for _ in my_set:
        num += _
    return num
