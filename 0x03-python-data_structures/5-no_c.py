#!/usr/bin/python3
def no_c(my_string):
    string_maker = my_string.translate({ord(m): None for m in 'cC'})
    return string_maker
