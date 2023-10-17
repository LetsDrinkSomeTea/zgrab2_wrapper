#!/bin/python3

def print_dict(d):
    """Prints a dictionary in a nice format"""
    for k, v in d.items():
        print(f"{k}: {v}")


def print_list(lst):
    """Prints a list in a nice format"""
    if len(lst) == 0:
        print("No successful ip/domain\n")
        return
    out = "successful ip/domain:"
    for item in lst:
        out += f'{item}, '
    print(out[:-2] + '\n')
