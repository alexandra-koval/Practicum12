def maxlist(a):
    """
    Returns the maximum element of a list of integers recursively.
    Returns None for an empty list.
    """
    if len(a) == 1:
        return a[0]
    if len(a) == 0:
        return None
    return max(a[0], maxlist(a[1:]))
