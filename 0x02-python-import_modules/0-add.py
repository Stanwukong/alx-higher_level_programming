#!/usr/bin/python3
# 0_add.py

if __name__ == "__main__":
    """Print the sum of a and b."""
    from add_0 import add

    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
