#!/usr/bin/python3
def to_uper(ch):
    if ord(ch) >= 97 and ord(ch) <= 122:
        return (ord(ch) - 32)
    else:
        return ord(ch)


def uppercase(str):
    str_new = ""
    for ch in str:
        str_new += "%c" % to_uper(ch)
    print("{:s}".format(str_new))
