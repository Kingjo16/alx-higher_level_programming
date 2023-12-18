#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    print_elem = 0
    for m in range(x):
        try:
            print("{:d}".format(my_list[m]), end="")
            print_elem += 1
        except (ValueError, TypeError):
            continue
    print()
    return (print_elem)
