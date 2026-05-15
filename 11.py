def ind_maxlist(a):
    """
    Returns the index of the maximum element in a list of integers
    recursively.
    """
    if a[len(a) - 1] == max(a):
        return len(a) - 1
    else:
        return ind_maxlist(a[:-1])
