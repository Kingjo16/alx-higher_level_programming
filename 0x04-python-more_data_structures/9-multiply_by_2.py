#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = {}
    for m, v in a_dictionary.items():
        new_dict.update({m: (v * 2)})
    return new_dict
