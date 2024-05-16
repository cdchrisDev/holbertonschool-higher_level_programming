#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
dig = abs(number) % 10
print(f"Last digit of {number} is ", end="")
if number < 0:
    dig = -dig
    
if dig < 6 and dig != 0:
    print(f"{dig} and is less than 6 and not zero")
elif dig == 0:
    print(f"{dig} and is 0")
else:
    print(f"{dig} and is greater than 5")