#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastd = number % 10
else:
    lastd = ((number * -1) % 10) * -1

message = "Last digit of %d is %d and is" % (number, lastd)

if lastd == 0:
    print(message, "0")
elif lastd > 5:
    print(message, "greater than 5")
else:
    print(message, "less than 6 and not 0")
