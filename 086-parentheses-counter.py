"""
Daily Coding Problem - 2019-01-02.

Given a string of parentheses, write a function to compute the minimum
number of parentheses to be removed to make the string valid (i.e. each
open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1.
Given thestring ")(", you should return 2, since we must remove all of them.
"""


def solve(str):
    """Count of parentheses to remove."""
    counter = 0
    for i in str:
        if i == "(":
            counter += 1
        elif i == ")" and counter > 0:
            counter -= 1
        else:
            counter += 1
    return counter


print(solve("()())()"))    # 1
print(solve(")("))    # 2
print(solve("((()()((()))))"))    # 0
