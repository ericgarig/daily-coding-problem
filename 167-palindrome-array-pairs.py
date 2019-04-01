"""
Daily Coding Problem - 2019-03-24.

Given a list of words, find all pairs of unique indices such that the
concatenation of the two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"], return
[(0, 1), (1, 0), (2, 3)].
"""


def solve(arr):
    """
    Get a list of unique index pairs that form a palindrome.

    O(n^2) since every word is compared with every other word.
    """
    result = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                test_str = "".join([arr[i], arr[j]])
                if test_str == test_str[::-1]:
                    result.append((i, j))
    return result


assert (solve(["code", "edoc", "da", "d"])) == [(0, 1), (1, 0), (2, 3)]
