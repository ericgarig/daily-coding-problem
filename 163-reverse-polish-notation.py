"""
Daily Coding Problem - 2019-03-20.

Given an arithmetic expression in Reverse Polish Notation, write a program to
evaluate it.

The expression is given as a list of numbers and operands. For example:
[5, 3, '+'] should return 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
should return 5, since it is equivalent to
((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.
"""
import operator


def solve(arr):
    """Given an array in reverse Polish notation, solve it."""
    exp_stack = []
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "%": operator.mod,
        "^": operator.xor,
    }
    for i in arr:
        if isinstance(i, (int, float)):
            exp_stack.append(i)
        else:
            second = exp_stack.pop()
            first = exp_stack.pop()
            exp_stack.append(ops[i](first, second))
    return exp_stack[0]


assert (
    solve([15, 7, 1, 1, "+", "-", "/", 3, "*", 2, 1, 1, "+", "+", "-"])
) == 5
assert solve([15, 4, 6, "*", "-"]) == -9
