#!/usr/bin/python3

def magic_calculation(a, b):
    totals = 0
    for m in range(1, 3):
        try:
            if m > a:
                raise Exception('Too far')
            totals += a ** b / m
        except Exception:
            totals = b + a
            break
        return totals
