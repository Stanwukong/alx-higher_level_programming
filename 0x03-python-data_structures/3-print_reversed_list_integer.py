#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    if isInstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{}".format(i))
