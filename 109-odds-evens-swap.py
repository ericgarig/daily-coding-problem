"""
Daily Coding Problem - 2019-01-25.

Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and
2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.

Bonus: Can you do this in one line?
"""


def solve(k):
    """Swap the odds-evens bits of 8-bit integer."""
    result = ''
    for i in range(len(k)):
        if i % 2 == 1:
            result += k[i] + k[i - 1]
    return result


def solve_short(k):
    """One-liner of solve function."""
    return ''.join([k[i] + k[i - 1] for i in range(len(k)) if i % 2 == 1])


print(solve('10101010') == '01010101')
print(solve('11100010') == '11010001')

print(solve_short('10101010') == '01010101')
print(solve_short('11100010') == '11010001')
