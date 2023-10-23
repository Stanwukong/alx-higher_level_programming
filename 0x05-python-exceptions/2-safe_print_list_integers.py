#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    no_of_elem = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            no_of_elem += 1
        except (TypeError, ValueError, IndexError):
            continue
    print("")
    return no_of_elem
