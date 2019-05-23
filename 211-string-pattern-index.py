"""
Daily Coding Problem - 2019-05-07.

Given a string and a pattern, find the starting indices of all occurrences of
the pattern in the string. For example, given the string "abracadabra" and the
pattern "abr", you should return [0, 7].
"""


def solve(st="", p=""):
    """Get the starting index of each pattern p in string st."""
    indices = []
    for i in range(len(st) - len(p) + 1):
        if st[i : i + len(p)] == p:
            indices.append(i)
    return indices


assert (solve("abracadabra", "abr")) == [0, 7]
assert (solve("aabaaab", "ab")) == [1, 5]
assert (solve("aabaaab", "z")) == []
assert (solve("aabab", "aab")) == [0]
