#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()
    for locker in keys:
        print("{}: {}".format(locker, a_dictionary[locker]))
