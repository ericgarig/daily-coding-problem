"""
Daily Coding Problem - 2019-06-09.

The Sieve of Eratosthenes is an algorithm used to generate all prime
numbers smaller than N. The method is to take increasingly larger prime
numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark
[4, 6, 8, ...] (multiples of two), then [6, 9, 12, ...] (multiples
of three), and so on. Once we have done this for all primes less than N,
the unmarked numbers that remain will be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is,
without taking N as an input).
"""
from math import sqrt


def solve(k):
    """Implement the Sieve of Eratosthenes."""
    arr = list(range(k + 1))
    for i in range(2, (k // 2) + 1):
        mult = 2
        while i * mult <= k:
            arr[i * mult] = None
            mult += 1
        # print(i, arr)
    arr = [i for i in arr if i is not None]
    arr = arr[2:]
    return arr


def gen_next_prime():
    """Generator for primes."""
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


def is_prime(n):
    """Determine if the number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n) + 1), 2):
        if n % i == 0:
            return False
    return True


assert solve(10) == [2, 3, 5, 7]
assert solve(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


num = gen_next_prime()
assert next(num) == 2
assert next(num) == 3
assert next(num) == 5
assert next(num) == 7
assert next(num) == 11
assert next(num) == 13
