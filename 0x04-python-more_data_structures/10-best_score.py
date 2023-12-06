#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        my_list = list(a_dictionary.keys())
        score = 0
        leader = ""
        for ind in my_list:
            if a_dictionary[ind] > score:
                score = a_dictionary[ind]
                leader = ind
        return leader
