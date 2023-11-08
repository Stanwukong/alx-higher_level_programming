#!/usr/bin/python3
"""This module defines a function that saves its arguments into a file."""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    existing_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_list = []

existing_list.extend(sys.argv[1:])

save_to_json_file(existing_list, "add_item.json")
