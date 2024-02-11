#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
div = abs(number) % 10
if number < 0:
	div = -div
print("Last digit of {} is {} and is ".format(number, div), end="")
if div > 5:
    print("greater than 5")
elif div == 0:
    print("0")
else:
    print("less than 6 and not 0")
