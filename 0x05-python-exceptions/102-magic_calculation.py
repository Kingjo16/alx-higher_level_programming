#!/usr/bin/python3

def magic_calculation(a, b):
    totals = 0
    for m in range(1, 4):
        try:
            if (m > a):
                raise (Exception('Too far'))
            else:
                totals = (((a ** b) / m) + totals)
        except (Exception):
            totals = (b + a)
            break
    return (totals)
