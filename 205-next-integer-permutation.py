"""
Daily Coding Problem - 2019-05-01.

Given an integer, find the next permutation of it in absolute order. For
example, given 48975, the next permutation would be 49578.
"""


def solve(k):
    """Find the next largest permutation."""
    k_list = [int(i) for i in str(k)]
    stack = []
    for i in k_list[::-1]:
        if not stack or int(stack[-1]) < i:
            stack.append(i)
        else:
            break
    pivot_pos = len(k_list) - len(stack) - 1
    for i in range(len(stack)):
        if k_list[pivot_pos] < stack[i]:
            k_list[pivot_pos], stack[i] = stack[i], k_list[pivot_pos]
            break
    k_list[len(stack) - 1 :] = stack
    return int("".join(map(str, k_list)))


assert (solve(48975)) == 49578
assert (solve(42864)) == 44268
assert (solve(45864)) == 46458
