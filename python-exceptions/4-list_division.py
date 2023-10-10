#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nw_list = [0 for _ in range(list_length)]
    for index in range(list_length):
        try:
            nw_list[index] = my_list_1[index] / my_list_2[index]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
    return nw_list
