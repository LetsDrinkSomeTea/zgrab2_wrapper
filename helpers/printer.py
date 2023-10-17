def print_dict(d):
    """Prints a dictionary in a nice format"""
    for k, v in d.items():
        print(f"{k}: {v}")
    print()


def print_list(l):
    """Prints a list in a nice format"""
    out = ""
    for item in l:
        out += f'{item}, '
    print(out[:-2])
