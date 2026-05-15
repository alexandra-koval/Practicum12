def search(a, x):
    """
    Returns 1 if integer x is present in list a, 0 otherwise.
    """
    if len(a) == 0:
        return 0
    if a[0] == x:
        return 1
    return search(a[1:], x)


print(search([1, 2, 3, 4, 5], 3))
