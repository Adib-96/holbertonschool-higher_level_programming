#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [_ for _ in my_list]
    for element in my_list:
        if element == search:
            new_list[element] = replace
    return new_list