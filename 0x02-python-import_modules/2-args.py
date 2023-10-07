#!/usr/bin/python3
# 2-args.py

import sys

if __name__ == "__main__":
    """Prints the number of and list of its arguments"""
    numArgs = len(sys.argv) - 1

    if numArgs == 0:
        print("{} arguments.".format(numArgs))
    elif numArgs == 1:
        print("{} argument:".format(numArgs))
    else:
        print("{} arguments:".format(numArgs))

    for arg in range(numArgs):
        print("{} : {}".format(arg + 1, sys.argv[arg + 1]))
