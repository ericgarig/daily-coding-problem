"""
Daily Coding Problem - 2018-10-20.

Given an integer k and a string s, find the length of the longest
substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k
distinct characters is "bcb".
"""


def longest_substring(num_chars, some_str):
    """Find the longest substring with up to num_chars unique chars."""
    if len(some_str) == 0:
        return 0

    count = 0
    sub_str = ''
    for i in some_str:
        if i in sub_str:
            sub_str += i
        elif count < num_chars:
            count += 1
            sub_str += i
        else:
            break
    return max(len(sub_str), longest_substring(num_chars, some_str[1:]))


print(longest_substring(2, "abcba"))    # 3 ( bcb )
print(longest_substring(3, "abcba"))    # 5 ( abcba )
print(longest_substring(2, "aabcccabba"))    # 4 ( bccc )
