"""
Daily Coding Problem - 2018-10-17.

Implement a job scheduler which takes in a function f and an integer n,
and calls f after n milliseconds.
"""
import time


def say_hi():
    """A sample function that greets you."""
    return 'Hello'


def delayed_call(f, n):
    """Call the specified function after a delay."""
    time.sleep(n)
    return eval(f + '()')


delayed_call('say_hi', 3)
