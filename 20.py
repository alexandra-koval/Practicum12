def comp(a, b, m, n):
    """
    Returns the length of the longest common subsequence (LCS)
    of strings a and b with lengths m and n.
    """
    if m == 0 or n == 0:
        return 0
    if a[m - 1] == b[n - 1]:
        return 1 + comp(a, b, m - 1, n - 1)
    else:
        return max(comp(a, b, m - 1, n), comp(a, b, m, n - 1))
