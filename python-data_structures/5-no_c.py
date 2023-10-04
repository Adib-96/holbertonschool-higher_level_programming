#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for c in my_string:
        if (c == "c") or (c == "C"):
            continue
        else:
            new_str = new_str + c
    return new_str
