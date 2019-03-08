"""
Daily Coding Problem - 2019-02-27.

You're given a string consisting solely of (, ), and *.
* can represent either a (, ), or an empty string. Determine whether the
parentheses are balanced.

For example, '(()*' and '(*)' are balanced. ')*('' is not balanced.
"""


def solve(some_str="", arr=None):
    """Given a string, determine if the parenthesis are balanced."""
    if not arr:
        arr = list(some_str)
    start_arr = arr[:]
    for i in range(len(arr)):
        if arr[i] == "*":
            arr[i] = "("
            if solve(arr=arr):
                return True
            arr = start_arr[:]
            arr[i] = ")"
            if solve(arr=arr):
                return True
            arr = start_arr[:]
            arr[i] = ""
            if solve(arr=arr):
                return True
    return is_balanced(arr)


def is_balanced(arr):
    """Helper function that checks if the parenthesis are balanced."""
    counter = 0
    for i in arr:
        if i == "(":
            counter += 1
        elif i == ")":
            counter -= 1
        if counter < 0:
            return False
    return counter == 0


assert (solve("(()*")) == True
assert (solve("(*)")) == True
assert (solve(")*(")) == False
assert (solve("(((**(**")) == True
assert (solve("(((**(*)")) == True
assert (solve("(((**()")) == False
assert (solve("(**")) == True
assert (solve("*")) == True
assert (solve(")**")) == False
