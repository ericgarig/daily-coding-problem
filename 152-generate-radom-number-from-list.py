"""
Daily Coding Problem - 2019-03-09.

You are given n numbers as well as n probabilities that sum up to 1.
Write a function to generate one of the numbers with its corresponding
probability.

For example, given the numbers [1, 2, 3, 4] and probabilities
[0.1, 0.5, 0.2, 0.2], your function should return 1 10% of the time,
2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.
"""
import random


def solve(arr=[], pct=[]):
    """Generate a random number from a list of numbers their probabilties."""
    r = random.random()
    total = 0
    for i in range(len(pct)):
        total += pct[i]
        if total >= r:
            return arr[i]
    return arr[-1]


num_list = [1, 2, 3, 4]
percentages = [0.1, 0.5, 0.2, 0.2]
d = {i: 0 for i in num_list}
for i in range(100):
    random_num = solve(num_list, percentages)
    d[random_num] += 1
print(d)
