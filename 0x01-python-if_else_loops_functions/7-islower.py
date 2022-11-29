#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        print("{:c} is lower".format(c), end="")
    else:
        print("{:c} i upper".format(c), end="")
