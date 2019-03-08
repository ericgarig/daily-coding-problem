"""
Daily Coding Problem - 2019-03-05.

Gray code is a binary code where each successive value differ in only
one bit, as well as when wrapping around. Gray code is common in
hardware so that we don't see temporary spurious values during transitions.

Given a number of bits n, generate a possible gray code for it.

For example, for n = 2, one gray code would be [00, 01, 11, 10].
"""


def solve(k):
    """Generate gray code for k bits."""
    if k == 1:
        return ["0", "1"]
    result = []
    prev = solve(k - 1)
    result.extend(["".join(["0", i]) for i in prev])
    result.extend(["".join(["1", i]) for i in reversed(prev)])
    return result


assert (solve(1)) == ["0", "1"]
assert (solve(2)) == ["00", "01", "11", "10"]
assert (solve(3)) == ["000", "001", "011", "010", "110", "111", "101", "100"]
assert (solve(4)) == [
    "0000",
    "0001",
    "0011",
    "0010",
    "0110",
    "0111",
    "0101",
    "0100",
    "1100",
    "1101",
    "1111",
    "1110",
    "1010",
    "1011",
    "1001",
    "1000",
]
