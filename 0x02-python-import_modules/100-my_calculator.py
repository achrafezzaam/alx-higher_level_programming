#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import exit, argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == '+':
            print("{}".format(add(a, b)))
        elif argv[2] == '-':
            print("{}".format(sub(a, b)))
        elif argv[2] == '*':
            print("{}".format(mul(a, b)))
        elif argv[2] == '/':
            print("{}".format(div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
