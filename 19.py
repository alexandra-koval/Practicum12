def count(a, b):
    """
    Returns the number of squares that can be cut from a rectangle
    with sides a and b by repeatedly cutting off the largest possible square.
    """
    if a == 0 or b == 0:
        return 0
    if a == b:
        return 1
    if a > b:
        return 1 + count(a - b, b)
    else:
        return 1 + count(a, b - a)
