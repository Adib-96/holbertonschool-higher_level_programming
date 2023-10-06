#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]
    if len(my_list) == 0:
        return None
    for num in range(1, len(my_list)):
        if max < my_list[num]:
            max = my_list[num]
    return int(max)
