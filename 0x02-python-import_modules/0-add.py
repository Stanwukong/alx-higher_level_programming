#!/usr/bin/python3

""" Imports the function from add_0.py

   prints the result of the addition 1 + 2 = 3

   Assign:
         a = 1, b = 2
"""
if __name__ == "__main__":

    from add_0 import add

    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
