"""
Daily Coding Problem - 2019-01-18.

Given a list of integers and a number K, return which contiguous
elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should
return [2, 3, 4].
"""


def solve(arr=[], k=0):
    """Get the subarray that adds up to k."""
    total = 0
    result = []
    for i in arr:
        if total == k:
            return result
        total += i
        result.append(i)
        if total + i > k:
            while total > k:
                total -= result.pop(0)
    if total != k:
        return None
    return result


print(solve([1, 2, 3, 4, 5], 9))    # [2, 3, 4]
print(solve([1, 2, 3, 4, 5], 8))    # None
print(solve([1, 3, 3, 4, 5], 9))    # [4, 5]
