#!/usr/bin/python3

"""

Modules that adds all arguments to a python list,
and then save them to a file

"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

open("add_item.json", "a")

my_list = load_from_json_file("add_item.json")
my_list.append(sys.argv[1:])

save_to_json_file(my_list, "add_item.json")
