#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_one = []
    for i in my_list:
        if i % 2 == 0:
            new_one.append(True)
            return new_one
        else:
            new_one.append(False)
            return new_one
