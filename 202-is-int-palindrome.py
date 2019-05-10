"""
Daily Coding Problem - 2019-04-28.

Write a program that checks whether an integer is a palindrome. For example,
121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert
the integer into a string.
"""


def solve(k, magnitude=0):
    """Determine if k is a palindrome without converting it to a string."""
    if k < 10:
        return True
    if not magnitude:
        magnitude = get_int_magnitude(k)
    if (k // (10 ** magnitude)) != (k % 10):
        return False
    return solve(k % (10 ** magnitude) // 10, magnitude=magnitude - 1)


def get_int_magnitude(k):
    """Get the magnitude of the specified integer."""
    magnitude = 0
    while 9 < k:
        k = k // 10
        magnitude += 1
    return magnitude


assert (solve(121)) is True
assert (solve(888)) is True
assert (solve(678)) is False
