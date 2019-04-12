"""
Daily Coding Problem - 2019-04-07.

Given a string, split it into as few strings as possible such that each string
is a palindrome.

For example, given the input string racecarannakayak,
return ["racecar", "anna", "kayak"].

Given the input string abc, return ["a", "b", "c"].
"""


def solve(s):
    """Split string into as few palindromes as possible."""
    result = []
    while s:
        for i in range(len(s), 0, -1):
            if s[0] == s[i - 1]:
                start = 0
                end = i - 1
                while start < end and start < len(s) and 0 < end:
                    if s[start] != s[end]:
                        break
                    start += 1
                    end -= 1
                else:
                    result.append(s[:i])
                    s = s[i:]
                    break
    return result


assert (solve("racecarannakayak")) == ["racecar", "anna", "kayak"]
assert (solve("abc")) == ["a", "b", "c"]
