u"""
Daily Coding Problem - 2019-02-23.

Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16,
return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
"""


def solve(n=0):
    """Find the minimum number of coints needed to make n cents."""
    coins = 0
    denominations = [25, 10, 5, 1]
    for i in denominations:
        one_coin_type = n // i
        coins += one_coin_type
        n -= i * one_coin_type
    return coins


print(solve(16))  # 3
print(solve(80))  # 4
print(solve(79))  # 7
print(solve(41))  # 4
