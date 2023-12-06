#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    for ind_elem in my_list:
        if ind_elem == search:
            new_list.append(replace)
        else:
            new_list.append(ind_elem)
    return new_list
