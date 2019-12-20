"""
Daily Coding Problem - 2019-05-29.

Implement the function fib(n), which returns the nth number in the
Fibonacci sequence, using only O(1) space.
"""


def solve(n):
    """
    Determine the nth-fibonacci number using linear space.

    NOTE:
    fib(n) = fib(n-1) + fib(n-2), so we need to store just the last 2
    numbers.
    """
    if n <= 1:
        return n
    current, last, two_ago = 0, 1, 0
    for i in range(1, n):
        current = last + two_ago
        two_ago = last
        last = current
    return current


assert solve(1) == 1
assert solve(6) == 8
assert solve(13) == 233
