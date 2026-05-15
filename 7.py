def nod(a, b):
    """
    Returns the greatest common divisor of two natural numbers
    using Euclid's algorithm.
    """
    if b == 0:
        return a
    else:
        return nod(b, a % b)
