#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
string1 = ("Last digit of {:d} is".format(number))

if lastDigit > 5:
    string2 = "and is greater than 5"
elif lastDigit == 0:
    string2 = "and is 0"
else:
    string2 = "and is less than 6 and not 0"

if lastDigit > 5:
    print("{:s} {:d}".format(string1, lastDigit), string2)
elif lastDigit == 0:
    print("{:s} {:d}".format(string1, lastDigit), string2)
else:
    print("{:s} {:d}".format(string1, lastDigit), string2)
