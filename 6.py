def degree5(n):
    """Returns the exponent if n is a power of 5, otherwise returns -1."""
    if n == 1:
        return 0
    if n % 5 != 0:
        return -1
    result = degree5(n // 5)
    return -1 if result == -1 else 1 + result
