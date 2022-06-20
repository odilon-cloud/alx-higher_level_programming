#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element = 0
    try:
        while element in range(x):
            print(my_list[element], end='')
            element += 1
    except IndexError:
        None
    print("")
    return(element)
