#!/usr/bin/python3

""" Imports the function from add_0.py

   prints the result of the addition 1 + 2 = 3

   Assign:
         a = 1, b = 2
"""
import add_0

a = 1
b = 2
result = add_0.add(a, b)
print("{:d} + {:d} = {:d}".format(a, b, result))
