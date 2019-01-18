"""
Daily Coding Problem - 2018-11-23.

Given a array of numbers representing the stock prices of a company in
chronological order, write a function that calculates the maximum profit
you could have made from buying and selling that stock once. You must
buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you
could buy the stock at 5 dollars and sell it at 10 dollars.
"""


def solve(arr):
    """
    Return the max profit.

    Inefficient brute force solution. Has a run-time of O(n^2).
    """
    profit = 0
    for i, buy in enumerate(arr[:len(arr) - 1]):
        for sell in arr[i + 1:]:
            if (sell - buy) > profit:
                profit = sell - buy
    return profit


def solve_smart(arr):
    """Better approach."""
    result = None
    low = None
    for p in arr:
        if low is None or low > p:
            # found a new lower price
            low = p
        elif result is None or result < p - low:
            result = p - low
    return result


print(solve([9, 11, 8, 5, 7, 10]))    # 5
print(solve_smart([9, 11, 8, 5, 7, 10]))    # 5
