def sum_progress(a1, r, n):
    """
    Returns the sum of the first n terms of an arithmetic progression
    using recursion.
    """
    if n == 1:
        return a1
    else:
        return (a1 + (n - 1) * r) + sum_progress(a1, r, n - 1)
