#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv) - 1
    count = 0
    for i in range(argc):
        count += int(sys.argv[i + 1])
    print(count)
