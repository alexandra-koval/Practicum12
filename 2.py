def count(n):
    '''Returns number of digits in n using recursion'''
    if n < 10:
        return 1
    else:
        return 1 + count(n // 10)
