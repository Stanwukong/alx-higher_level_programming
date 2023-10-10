#!/usr/bin/python3

import sys

if __name__ == "__main__":
    numArgs = len(sys.argv) - 1

    if numArgs == 0:
        print("0 arguments.")
    elif numArgs == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(numArgs))

    for arg in range(1, numArgs + 1):
        print("{}: {}".format(arg, sys.argv[arg]))
