"""
Daily Coding Problem - 2019-04-02.

Determine whether there exists a one-to-one character mapping from one
string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map
a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two
characters.
"""


def solve(s1, s2):
    """Determine if there can a mapping from one string to another."""
    if len(s1) != len(s2):
        return False
    mapping = {}
    for i in range(len(s1)):
        if s1[i] not in mapping:
            mapping[s1[i]] = s2[i]
        elif mapping[s1[i]] != s2[i]:
            return False
    return True


assert (solve("abc", "bcd")) is True
assert (solve("foo", "bar")) is False
