"""
Daily Coding Problem - 2019-03-18.

Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000,
return 0000 1111 0000 1111 0000 1111 0000 1111.
"""


def solve(num_str):
    """Given a binary string, reverse the bits."""
    return "".join(reversed(list(num_str)))


assert (
    solve("11110000111100001111000011110000")
) == "00001111000011110000111100001111"
