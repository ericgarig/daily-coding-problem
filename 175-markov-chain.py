"""
Daily Coding Problem - 2019-04-01.

You are given a starting state start, a list of transition probabilities for a
Markov chain, and a number of steps num_steps. Run the Markov chain starting
from start for num_steps and compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the
following transition probabilities:

[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]

One instance of running this Markov chain might produce
{ 'a': 3012, 'b': 1656, 'c': 332 }.
"""
import random


def convert_map(arr):
    """Convert Markov tuple map to a pair of nested lists."""
    list_prob = {}
    list_state = {}
    state_start = arr[0][0]
    one_prob = []
    one_state = []
    running_total = 0
    for i in arr:
        if i[0] != state_start:
            list_prob[state_start] = one_prob
            list_state[state_start] = one_state
            state_start = i[0]
            running_total = 0
            one_prob = []
            one_state = []
        running_total += i[2]
        one_prob.append(running_total)
        one_state.append("{}{}".format(i[0], i[1]))
    else:
        list_prob[state_start] = one_prob
        list_state[state_start] = one_state
    return [list_prob, list_state]


def solve(start, arr, num_steps):
    """Run Markov chain."""
    [list_prob, list_state] = convert_map(arr)
    result = {}
    for i in range(num_steps):
        prob = random.random()
        for i in range(len(list_prob[start])):
            if list_prob[start][i] > prob:
                if start in result:
                    result[start] += 1
                else:
                    result[start] = 1
                start = list_state[start][i][1]
    return result


print(
    solve(
        "a",
        [
            ("a", "a", 0.9),
            ("a", "b", 0.075),
            ("a", "c", 0.025),
            ("b", "a", 0.15),
            ("b", "b", 0.8),
            ("b", "c", 0.05),
            ("c", "a", 0.25),
            ("c", "b", 0.25),
            ("c", "c", 0.5),
        ],
        5000,
    )
)
