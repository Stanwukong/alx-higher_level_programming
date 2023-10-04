#!/usr/bin/python3
def uppercase(str):
    for s in str:
        value = ord(str)
        if value >= 97 and value <= 122:
            value -= 32
        print("{:c}".format(value), end='')
    print("")
