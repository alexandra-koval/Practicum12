def count(n):
    '''Returns a raised to the power of n using recursion.'''
    if n < 10:
        return 1
    else:
        return 1 + count(n // 10)
