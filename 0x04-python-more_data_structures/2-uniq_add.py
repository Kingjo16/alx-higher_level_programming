#!/usr/bin/pyhton3

def uniq_add(my_list=[]):
    new_list = set(my_list)
    sum = 0
    for new_num in new_list:
        sum += new_num
    return sum
