u"""
Daily Coding Problem - 2019-01-18.

Given an even number (greater than 2), return two prime numbers whose
sum will be equal to the given number.

A solution will always exist. See Goldbach’s conjecture.

Example:
    Input: 4
    Output: 2 + 2 = 4

If there are more than one solution possible, return the
lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution
with c <= d, then

[a, b] < [c, d]
If a < c OR a==c AND b < d.
"""


def solve(k):
    """Return two primes whose sum is k."""
    min_sol = [k, k]
    primes = get_primes(k)
    for i in primes:
        for j in primes:
            if i + j == k:
                min_prime = min(i, j)
                max_prime = max(i, j)
                solution = [min_prime, max_prime]
                if min_prime < min_sol[0]:
                    min_sol = solution
    if min_sol == [k, k]:
        return None
    return min_sol


def get_primes(k):
    """Get all the primes less than k."""
    primes = []
    for i in range(2, k):
        if is_prime(i):
            primes.append(i)
    return primes


def is_prime(n):
    """
    Determine if the number is a prime.

    Algotrithm taken from:
    https://stackoverflow.com/questions/1801391/what-is-the-best-algorithm-for-checking-if-a-number-is-prime
    """
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


for i in range(4, 100, 2):
    print(i, solve(i))
