#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """function that prints an integer with "{:d}".format()."""
    num = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            num += 1
        except IndexError:
            break
    print()
    return(num)
