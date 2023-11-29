#!/usr/bin/python3

def fizzbuzz():
    for fnumber in range(1, 101):
        if fnumber % 3 == 0 and fnumber % 5 == 0:
            print("FizzBuzz ", end="")
        elif fnumber % 3 == 0:
            print("Fizz ", end="")
        elif fnumber % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(fnumber), end="")
