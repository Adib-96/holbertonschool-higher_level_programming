#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    counter = len(my_list)-1
    while counter >= 0:
        print('{:d}'.format(my_list[counter]))
        counter -= 1
