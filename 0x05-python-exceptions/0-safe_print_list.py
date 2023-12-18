#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    printed_elem = 0
    for m in range(x):
        try:
            print("{}".format(my_list[m]), end="")
            printed_elem += 1
        except IndexError:
            break

    print("")
    return (printed_elem)
