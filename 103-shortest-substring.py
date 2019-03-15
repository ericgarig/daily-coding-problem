"""
Daily Coding Problem - 2019-01-19.

Given a string and a set of characters, return the shortest substring
containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters
{a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.
"""

# import timeit


def solve_brute_force(s="", chars={}):
    """Determine the shortest substring that contains a set of chars."""
    if len(s) < len(chars):
        return None
    substrings = []
    for i in range(len(s)):
        if s[i] in chars:
            for j in range(i, len(s)):
                if chars.issubset(set(s[i : j + 1])):
                    substrings.append(s[i : j + 1])
                    break
    if not substrings:
        return None
    return min(substrings, key=len)


def solve_sliding_pointers(s="", chars={}):
    """
    Find the shortest substring by checking between sliding pointers.

    About 5 magnitudes faster than brute-force approach
    """
    if len(s) < len(chars):
        return None
    for i in range(len(s)):
        if s[i] in chars:
            left, right = i, i + len(chars) - 1
            break
    else:
        return None
    result = s
    while right < len(s):
        test_str = s[left : right + 1]
        while chars.issubset(set(test_str)):
            if len(test_str) < len(result):
                result = test_str
            left += 1
            test_str = s[left : right + 1]
        right += 1
    if result == s:
        return None
    return result


# start = timeit.default_timer()
assert (solve_brute_force("figehaeci", {"a", "e", "i"})) == "aeci"
# stop = timeit.default_timer()
# print('Time: ', stop - start)


# start = timeit.default_timer()
assert (solve_sliding_pointers("figehaeci", {"a", "e", "i"})) == "aeci"
# stop = timeit.default_timer()
# print('Time: ', stop - start)
