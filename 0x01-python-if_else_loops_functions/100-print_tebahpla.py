#!/usr/bin/python3
i = 0
for c in range(122, 96, -1):
    print("{}".format(chr(c - i)), end="")
    if i == 0:
        i = 32
    else:
        i = 0
