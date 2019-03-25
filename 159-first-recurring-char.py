"""
Daily Coding Problem - 2019-03-16.

Given a string, return the first recurring character in it, or null if
there is no recurring character.

For example, given the string "acbbac", return "b".
Given the string "abcdef", return null.
"""


def solve(n):
    """Return first recurring character in a string."""
    unique_letters = {}
    for i in n:
        if i in unique_letters.keys():
            return i
        unique_letters[i] = 1
    return None


assert (solve("acbbac")) == "b"
assert (solve("abcdef")) is None
