def fib(k):
    """Returns the k-th Fibonacci number using recursion."""
    if k == 1:
        return 0
    elif k == 2:
        return 1
    else:
        return fib(k - 1) + fib(k - 2)
