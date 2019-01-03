"""
Daily Coding Problem - 2018-10-19.

There exists a staircase with N steps, and you can climb up either
1 or 2 steps at a time. Given N, write a function that returns the
number of unique ways you can climb the staircase. The order of the
steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

BONUS: What if, instead of being able to climb 1 or 2 steps at a time,
you could climb any number from a set of positive integers X?
E.g., if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""


def unique_climb(num_steps):
    """Given staircase of N steps be climbed 1 or 2 steps at a time."""
    return fib(num_steps + 1)


def fib(n):
    """Recursively get teh n-th dibonacci number."""
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def unique_climb_m(num_steps, max_steps):
    """Given a max number of steps, how many ways can the stairs be climbed."""
    num_steps += 1
    # Creates list res witth all elements 0
    res = [0 for x in range(num_steps)]
    res[0], res[1] = 1, 1

    for i in range(2, num_steps):
        j = 1
        while j <= max_steps and j <= i:
            res[i] = res[i] + res[i - j]
            j = j + 1
    return res[num_steps - 1]


print(unique_climb(4))    # 5
print(unique_climb_m(4, 2))    # 5
print(unique_climb_m(4, 3))    # 7
