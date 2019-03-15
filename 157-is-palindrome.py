"""
Daily Coding Problem - 2019-03-14.

Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to
form racecar, which is a palindrome. daily should return false, since
there's no rearrangement that can form a palindrome.
"""


def solve(n):
    """Determine there is permutation of the string to make a palindrome."""
    unique_letters = {}
    for i in n:
        if i in unique_letters.keys():
            del unique_letters[i]
        else:
            unique_letters[i] = 1
    if len(unique_letters) < 2:
        return True
    return False


assert (solve("carrace")) is True
assert (solve("daily")) is False
