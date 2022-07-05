#!/usr/bin/python3
"""File name : 1-my_list.py
    It is not allowed to import any module
"""


class MyList(list):
    """a subclass of list"""

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
