#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = number
last_dgt = temp % 10
if number < 0:
    temp = -1 * number
    last_dgt = -1 * (temp % 10)
output = f"Last digit of {number:d} is {last_dgt:d} "
if last_dgt > 5:
    output = output + "and is greater than 5"
else:
    if last_dgt == 0:
        output = output + "and is 0"
    else:
        output = output + "and is less than 6 and not 0"
print(output)
