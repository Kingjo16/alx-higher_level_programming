#!/usr/bin/python3
"""Listed int. Algoritem."""


def find_peak(list_of_integers):
    """Find a peak in List OF INTEGER."""
    if not list_of_integers:
        return None

    given_l = 0
    high = len(list_of_integers) - 1

    while given_l < high:
        middle_num = (given_l + high) // 2

        if list_of_integers[middle_num] < list_of_integers[middle_num + 1]:
            given_l = middle_num + 1
        else:
            high = middle_num

    return list_of_integers[given_l]
