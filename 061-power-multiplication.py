"""
Daily Coding Problem - 2018-12-08.

Implement integer exponentiation. That is, implement the pow(x, y)
function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
"""


def power(base, exp):
    """Integer exponentiation, done better than repeated multiplication."""
    if exp == 1:
        return base
    elif exp % 2 == 0:
        return power(base * base, exp // 2)
    else:
        return base * power(base * base, exp // 2)


print(power(2, 10))    # 1024
