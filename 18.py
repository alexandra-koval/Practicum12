def simmetr(s, i, j):
    """
    Returns True if the substring of s from index i to index j
    (inclusive) is symmetric (palindrome), False otherwise.
    """
    if i >= j:
        return True
    if s[i] != s[j]:
        return False
    return simmetr(s, i + 1, j - 1)
