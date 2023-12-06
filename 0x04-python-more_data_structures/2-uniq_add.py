#!/usr/bin/pyhton3

def uniq_add(my_list=[]):
    new_list = []
    sum = 0
    for new_num in my_list:
        if new_num not in new_list:
            sum += new_num
            new_list.append(new_num)
    return sum
