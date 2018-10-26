"""
Daily Coding Problem - 2018-10-22.

Given a stream of elements too large to store in memory, pick a random
element from the stream with uniform probability.
"""
import random


def pick_random(stream):
    """
    Pick random element with uniform probability.

    This is a reservoir sampling algorithm.
    """
    random_element = None
    for i, e in enumerate(stream):
        if i == 0:
            random_element = e
        elif random.randint(1, i + 1) == 1:
            random_element = e
    return random_element


print(pick_random([]))    # None
print(pick_random([1]))    # 1
print(pick_random([1, 2, 3, 4, 5, 6, 7, 8, 9]))    # random value
