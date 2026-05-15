def pownum(a, n):
    '''Returns a raised to the power of n using recursion.'''
    if n == 0:
        return 1
    else:
        return a * pownum(a, n - 1)
