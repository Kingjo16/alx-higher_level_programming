#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    first_tu = tuple_a + (0, 0)
    second_tu = tuple_b + (0, 0)
    new_tuple = first_tu[0] + second_tu[0], first_tu[1] + second_tu[1]
    return new_tuple
