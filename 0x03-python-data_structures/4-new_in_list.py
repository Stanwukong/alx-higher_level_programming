#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        new = my_list.copy()
        new[idx] = element
        return (new)
    return my_list
