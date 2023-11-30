#!/usr/bin/python3

if __name__ == "__main__":
   
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

        operations = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(operations.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[3])
    print("{} {} {} = {}".format(num1, sys.argv[2], num2, operations[sys.argv[2]](num1, num2)))
