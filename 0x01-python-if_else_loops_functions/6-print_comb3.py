#!/usr/bin/python3

for fdigit in range(0, 10):
    for sdigit in range(fdigit + 1, 10):
        if fdigit == 8 and sdigit == 9:
            print("{}{}".format(fdigit, sdigit))
        else:
            print("{}{}".format(fdigit, sdigit), end=", ")
