"""
Daily Coding Problem - 2019-01-27.

Given a word W and a string S, find all starting indices in S which are
anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
"""


def solve(w="", s=""):
    """Given string s, get start indices of anagram w."""
    result = [i for i in range(0, len(s) - len(w)) if s[i : i + len(w)] == w]
    s = s[::-1]
    result.extend(
        [
            len(s) - len(w) - i
            for i in range(0, len(s) - len(w))
            if s[i : i + len(w)] == w
        ]
    )
    return result


assert (solve("ab", "abxaba")) == [0, 3, 4]
