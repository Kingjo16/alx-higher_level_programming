#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    count_of_arg = len(sys.argv) - 1
    if count_of_arg == 0:
        print("0 arguments.")
    elif count_of_arg == 1:
        print("1 argument:")
    else:
         print("{} arguments:".format(count_of_arg))

    for i in range(count_of_arg):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
