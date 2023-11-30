#!/usr/bin/python3

def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        comb = add(a, b)
        for index_arg in range(4, 6):
            comb = add (comb, index_arg)
            return (comb)
        else:
            return(sub(a, b))
