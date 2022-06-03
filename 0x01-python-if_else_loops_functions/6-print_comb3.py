#!/usr/bin/python3
n = 0
while n <= 89:
    if n % 10 == 0:
        n += 1 + n // 10
    print("{:02d}".format(n), end='\n' if n == 89 else ", ")
    n += 1
