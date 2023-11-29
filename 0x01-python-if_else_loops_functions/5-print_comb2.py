#!/usr/bin/python3
for R_num in range(0, 100):
    if R_num == 99:
        print("{}".format(R_num))
    else:
        print("{:02}".format(R_num), end=", ")
