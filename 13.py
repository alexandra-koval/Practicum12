def odd_list(a, n):
    """
    Returns a list of even values from list a containing n integers.
    """
    if n == 0:
        return []
    if a[0] % 2 == 0:
        return [a[0]] + odd_list(a[1:], n - 1)
    else:
        return odd_list(a[1:], n - 1)
