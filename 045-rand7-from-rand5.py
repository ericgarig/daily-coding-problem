"""
Daily Coding Problem - 2018-11-21.

Using a function rand5() that returns an integer from 1 to 5 (inclusive)
with uniform probability, implement a function rand7() that returns an
integer from 1 to 7 (inclusive).
"""
from random import randint


def rand5():
    """Return a random intereger from 1 to 5 ( inclusive )."""
    return randint(1, 5)


def rand7():
    """Return a random integer from 1 to 7 using rand5 function."""
    while True:
        result = 5 * rand5() + rand5() - 5
        if result <= 21:
            return result % 7 + 1


def test_rand5():
    """Check rand5 for uniform probability."""
    d = dict([(i, 0) for i in range(1, 6)])
    for i in range(1000):
        d[rand5()] += 1
    return d


def test_rand7():
    """Check rand 7 for uniform probability."""
    d = dict([(i, 0) for i in range(1, 8)])
    for i in range(1000):
        d[rand7()] += 1
    return d


print(test_rand5())
print(test_rand7())
