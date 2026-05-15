def combin(n, k):
    """
    Computes the number of combinations C(n, k) recursively
    using the formula C(n, k) = C(n-1, k-1) + C(n-1, k)
    """
    if k == 0 or k == n:
        return 1
    if k > n:
        return 0
    return combin(n - 1, k - 1) + combin(n - 1, k)
