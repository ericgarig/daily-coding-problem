"""
Daily Coding Problem - 2018-10-08.

Given a list of numbers and a number k,
return whether any two numbers from the list add up to k.

E.g.: given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17

Bonus: do it in one pass.
"""


def solve(the_list, k):
    """
    Base solution.

    Does multiple passes to determine if sum of any 2 numbers are add to k.
    O(n**2)
    """
    for i in the_list[:-1]:
        for j in the_list[1:]:
            if i + j == k:
                return True
    return False


def solve_single_pass(the_list, k):
    """
    Bonus.

    Does a single pass to determine if 2 numbers in a list add to k.
    O(n)
    """
    while len(the_list) > 0:
        i = the_list.pop()
        if (k - i) in the_list:
            return True
    return False


assert (solve([10, 15, 3, 7], 17)) is True
assert (solve([10, 15, 3, 7], 20)) is False
assert (solve([10, 15, 3, 7], 25)) is True

assert (solve_single_pass([10, 15, 3, 7], 17)) is True
assert (solve_single_pass([10, 15, 3, 7], 20)) is False
assert (solve_single_pass([10, 15, 3, 7], 25)) is True
