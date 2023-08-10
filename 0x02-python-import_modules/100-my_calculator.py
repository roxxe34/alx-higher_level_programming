#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    argc = len(sys.argv) - 1
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if operator != "+" and operator != "-" and operator != "*" and operator != "/":
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        elif operator == "+":
            print("{} {} {} = {}".format(a, operator, b, add(a, b)))
        elif operator == "-":
            print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
        elif operator == "*":
            print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
        elif operator == "/":
            print("{} {} {} = {}".format(a, operator, b, div(a, b)))
