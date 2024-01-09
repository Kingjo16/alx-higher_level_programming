#!/usr/bin/python3
"""Add a python list arument and put thrm in one filr."""
import sys
import os.path
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
if os.path.isfile(filename):
    item = load_from_json_file(filename)
else:
    item = []
item.extend(sys.argv[1:])
save_to_json_file(item, filename)
