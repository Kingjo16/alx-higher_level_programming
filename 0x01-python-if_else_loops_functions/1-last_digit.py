#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = abs(number) % 10
if number < 0:
    x = -x
print(f"Last digit of {number} is {x} and is ", end="")
if x > 5:
    print("greater than 5")
elif x == 0:
    print("0")
else:
    print("less than 6 and not 0")
