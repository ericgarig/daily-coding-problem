"""
Daily Coding Problem - 2019-01-04.

Implement division of two positive integers without using the division,
multiplication, or modulus operators. Return the quotient as an integer,
ignoring the remainder.
"""


def division(num, divisor):
    """Implement divison."""
    result = 0
    while num >= divisor:
        result += 1
        num -= divisor
    return result


print(division(4, 2))    # 2
print(division(7, 2))    # 3
print(division(4, 4))    # 1
print(division(3, 4))    # 0
print(division(100, 2))    # 50
