def digit_to_char(digit):
    """
    Converts a digit (0-15) to a character (0-9, A-F).
    """
    if digit < 10:
        return str(digit)
    else:
        return chr(ord('A') + digit - 10)


def ten_to_n(x, n):
    """
    Converts a natural number x from decimal to base n (2 ≤ n ≤ 16).
    Returns the result as a string.
    """
    if x == 0:
        return "0"
    if x < n:
        return digit_to_char(x)
    return ten_to_n(x // n, n) + digit_to_char(x % n)
