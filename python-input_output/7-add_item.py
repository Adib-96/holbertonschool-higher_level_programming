#!/usr/bin/python3
"""
adds all arguments to a Python list, and then save them to a file
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


# Function to add items to the list and save to the JSON file
def add_items_to_list_and_save(args):
    try:
        # Load existing items from "add_item.json" if it exists
        item_list = load_from_json_file("add_item.json")
    except:
        # If the file doesn't exist, create an empty list
        item_list = []

    # Add the command-line arguments to the list
    item_list.extend(args)

    # Save the updated list to "add_item.json"
    save_to_json_file(item_list, "add_item.json")

    print("Items added and saved successfully!")


if __name__ == "__main__":
    # Get command-line arguments excluding the script name
    arguments = sys.argv[1:]

    # Check if there are any arguments
    if arguments:
        add_items_to_list_and_save(arguments)
    else:
        print("Usage: python add_item.py [item1] [item2] ...")
