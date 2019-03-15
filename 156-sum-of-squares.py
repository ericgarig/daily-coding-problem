"""
Daily Coding Problem - 2019-03-13.

Given a positive integer n, find the smallest number of squared integers
which sum to n.

For example, given n = 13, return 2 since 13 = 3^2 + 2^2 = 9 + 4.

Given n = 27, return 3 since 27 = 3^2 + 3^2 + 3^2 = 9 + 9 + 9.
"""


def solve(n):
    """Find the smallest number of squared integeres that sum to n."""
    if n == 0:
        return 0
    largest = 1
    while largest ** 2 <= n:
        largest += 1

    for i in range(largest - 1, 0, -1):
        square = i ** 2
        if n >= square:
            return 1 + solve(n - square)
    else:
        return None


assert (solve(1)) == 1
assert (solve(2)) == 2
assert (solve(3)) == 3
assert (solve(4)) == 1
assert (solve(5)) == 2
assert (solve(6)) == 3
assert (solve(7)) == 4
assert (solve(8)) == 2
assert (solve(9)) == 1
assert (solve(10)) == 2
assert (solve(11)) == 3
assert (solve(12)) == 4
assert (solve(13)) == 2
assert (solve(27)) == 3
assert (solve(99)) == 4
assert (solve(100)) == 1
assert (solve(545)) == 2
