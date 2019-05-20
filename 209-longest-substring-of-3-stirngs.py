"""
Daily Coding Problem - 2019-05-05.

Write a program that computes the length of the longest common subsequence of
three given strings. For example, given "epidemiologist", "refrigeration", and
"supercalifragilisticexpialodocious", it should return 5, since the longest
common subsequence is "eieio".
"""


def solve_substring(a, b, c):
    """Find the length of longest common substring of 3 strings."""
    string_list = [a, b, c]
    shortest = min(string_list, key=len)
    string_list.remove(shortest)
    for i in range(len(shortest)):
        sub_list = get_substring_list(shortest, len(shortest) - i)
        for one_sub in sub_list:
            if one_sub in string_list[0] and one_sub in string_list[1]:
                return len(one_sub)


def get_substring_list(s, k):
    """For the specified string s and length k, get all substrings."""
    result = []
    for i in range(len(s) - k + 1):
        result.append(s[i : i + k])
    return result


def solve_subsequence(a, b, c):
    """Find the longest subsequence of the 3 specified strings."""
    return max(
        longest_subsequence_order_a(a, b, c),
        longest_subsequence_order_a(b, a, c),
        longest_subsequence_order_a(c, b, a),
    )


def longest_subsequence_order_a(a, b, c):
    """Find the longest subsequence based on the order of a."""
    result = []
    for i in range(len(a)):
        if a[i] in b and a[i] in c:
            result.append(a[i])
            b = b[b.index(a[i]) + 1 :]
            c = c[c.index(a[i]) + 1 :]
    return len(result)


assert (
    solve_substring(
        "epidemiologist", "refrigeration", "supercalifragilisticexpialodocious"
    )
) == 2
assert solve_substring("apple", "apple pie", "mappl") == 4


assert (
    solve_subsequence(
        "epidemiologist", "refrigeration", "supercalifragilisticexpialodocious"
    )
) == 5
assert (solve_subsequence("abc", "adbc", "acb")) == 2
assert (solve_subsequence("abcb", "adbcb", "acb")) == 3
