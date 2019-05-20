"""
Daily Coding Problem - 2019-05-05.

A Collatz sequence in mathematics can be defined as follows. Starting with any
positive integer:
if n is even, the next number in the sequence is n / 2
if n is odd, the next number in the sequence is 3n + 1

It is conjectured that every such sequence eventually reaches the number 1.
Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?
"""


# The conjecture is true. If there is at least one instance where an even
# number results in an even number, the effective change is 4n. This is bigger
# than 3n + 1, so eventually the number will hit 1. The once time there is an
# equilbrium is when k = 1 ( becase 4 * 1 == 3 * 1 + 1 )


mem_dict = {}


def collatz(k):
    """Calculate the next Collatz value for the specified input."""
    if k % 2 == 0:
        return k // 2
    return 3 * k + 1


def solve(k):
    """
    Generate the Collatz sequence for the specified value.

    Added a global memoization dict to improve performance.
    """
    num = 0
    k_seq = k
    while 1 < k_seq:
        if k_seq in mem_dict:
            num += mem_dict[k_seq]
            break
        k_seq = collatz(k_seq)
        num += 1
    mem_dict[k] = num
    return num


max_num = 0
max_input = 0
for i in range(1, 1000000):
    one_run = solve(i)
    if max_num < one_run:
        max_num = one_run
        max_input = i
print(max_input)
