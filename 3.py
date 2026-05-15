def progress(a1, r, n):
    """Returns the n-th term of an arithmetic progression using recursion."""
    if n == 1:
        return a1
    else:
        return r + progress(a1, r, n - 1)
