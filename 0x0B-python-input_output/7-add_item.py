#!/usr/bin/python3
""" 7-add_item.py """
import sys
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

ln = len(sys.argv) - 1
my_list = [0] * ln
for i in range(ln):
    my_list[i] = sys.argv[i + 1]
try:
    my_list = load_from_json_file("add_item.json") + my_list
except FileNotFoundError:
    pass
save_to_json_file(my_list, "add_item.json")
