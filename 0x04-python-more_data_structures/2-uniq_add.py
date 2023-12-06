#!/usr/bin/pyhton3

def uniq_add(my_list=[]):
    """
    Add's a function that add a unique list
    """
    new_list = set(my_list)
    sum = 0
    for newnum in new_list:
        sum += newnum
    return sum
