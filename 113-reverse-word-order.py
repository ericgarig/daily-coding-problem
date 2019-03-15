"""
Daily Coding Problem - 2019-01-29.

Given a string of words delimited by spaces, reverse the words in string.
For example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this
operation in-place?
"""


def solve(s=""):
    """Given a string s, reverse the order of the words."""
    arr = s.split(" ")
    for i in range(len(arr) // 2):
        tail_index = len(arr) - i - 1
        arr[i], arr[tail_index] = arr[tail_index], arr[i]
    return " ".join(arr)


assert (solve("hello world here")) == "here world hello"
