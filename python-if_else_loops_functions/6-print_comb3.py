#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i, 10):
        if j == i:
            continue
        elif i == 8:
            print(f"{i}{j}")
        else:
            print(f"{i}{j}, ", end="")
