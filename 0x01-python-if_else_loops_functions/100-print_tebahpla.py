#!/usr/bin/python3
i = 90
while i >= 65:
    n = i
    if (i % 2) == 0:
        n += 32
    print("{}".format(chr(n)), end="")
    i -= 1
