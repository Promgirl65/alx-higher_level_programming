#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return (None)
    big_val = my_list[0]

    for index in range(1, length):
        if my_list[index] > big_val:
            big val = my_list[index]

    return (big_val)
