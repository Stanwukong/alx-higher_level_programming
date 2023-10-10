#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    sum = 0
    numArgs = len(sys.argv) - 1
    for i in range(numArgs):
        sum += int(sys.argv[i + 1])
    print(sum)
