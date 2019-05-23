"""
Daily Coding Problem - 2019-05-08.

Spreadsheets often use this alphabetical encoding for its columns:
"A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id. For example,
given 1, return "A". Given 27, return "AA".
"""


def solve(k):
    """Given a number, return the alphabetical encoding"""
    if not k:
        return ""
    return "".join([solve(k // 26), chr(64 + (k % 26))])


assert (solve(1)) == "A"
assert (solve(27)) == "AA"
assert (solve(54)) == "BB"
