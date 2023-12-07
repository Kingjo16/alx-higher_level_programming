#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    com_scr = 0
    com_wig = 0

    for scr, wig in my_list:
        com_scr += scr * sig
        com_wig += wig

    return com_scr / com_wig if com_wig != 0 else 0
