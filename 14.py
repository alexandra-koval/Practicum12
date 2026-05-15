def numbers(x):
    """
    Prints the digits of a natural number x in reverse order,
    one digit per line.
    """
    if x < 10:
        print(x)
    else:
        print(x % 10)
        numbers(x // 10)


numbers(12345)
