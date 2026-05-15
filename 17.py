def is_prime_helper(x, divisor):
    """
    Recursively checks if x is divisible by any number from divisor to sqrt(x).
    """
    if divisor * divisor > x:
        return 1
    if x % divisor == 0:
        return 0
    return is_prime_helper(x, divisor + 1)


def function1(x):
    """
    Returns 1 if natural number x is prime, 0 otherwise.
    """
    if x <= 1:
        return 0
    if x == 2:
        return 1
    if x % 2 == 0:
        return 0
    return is_prime_helper(x, 3)
