#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_one = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_one.insert(i, True)
        else:
            new_one.insert(i, False)
    return new_one
