#!/usr/bin/python3
from sys import argv


def list_args(args_len):
    for i in range(1, args_len):
        print("{}: {}".format(i, argv[i]))


def style_args_count(args_len):
    if args_len == 0:
        print("0 arguments.")
    elif args_len == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(args_len))


if __name__ == "__main__":
    args_len = len(argv)
    style_args_count(args_len - 1)
    if args_len != 1:
        list_args(args_len)
