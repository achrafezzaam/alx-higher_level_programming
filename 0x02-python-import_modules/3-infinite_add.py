#!/usr/bin/python3
from sys import argv


def add_args():
    ans = 0
    for i in range(1, len(argv)):
        ans += int(argv[i])
    return ans


if __name__ == "__main__":
    print("{}".format(add_args()))
