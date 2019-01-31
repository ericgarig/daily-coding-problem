"""
Daily Coding Problem - 2019-01-30.

Given a string and a set of delimiters, reverse the words in the string
while maintaining the relative order of the delimiters. For example,
given "hello/world:here", return "here/world:hello"

Follow-up: Does your solution work for the following cases:
"hello/world:here/"
"hello//world:here"
"""
import re


def solve(s='', delim={}):
    """Reverse the order of the words, maintaining the order of delimiters."""
    arr = re.split('(\W)', s)
    start, end = 0, len(arr) - 1
    while start < end:
        if len(arr[start]) == 1:
            start += 1
        elif len(arr[end]) == 1:
            end -= 1
        else:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    return ''.join(arr)


print(solve('hello/world:here'))    # "here/world:hello"
print(solve('hello/world:here/'))    # "/here/world:hello"
print(solve('hello//world:here'))    # "here/world/:hello"
