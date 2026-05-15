def mod_number(a, b):
    """Returns the remainder of division of a by b using recursion."""
    if a < b:
        return a
    else:
        return mod_number(a - b, b)
