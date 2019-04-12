"""
Daily Coding Problem - 2019-04-04.

Alice wants to join her school's Probability Student Club. Membership dues are
computed via one of two simple probabilistic games.

The first game: roll a die repeatedly. Stop rolling once you get a five
followed by a six. Your number of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five followed by
a five.

Which of the two games should Alice elect to play? Does it even matter? Write a
program to simulate the two games and calculate their expected value.
"""
from random import randint


"""
Alice should play the second game.
Although it may seem at first that each roll is independent and has a 1/6
chance, the order of the rolls matters.
"""


def dice_roll(first_roll, second_roll):
    """Return the number of rolls before rolling a 5 followed by 6."""
    num_rolls = 0
    is_five = False
    while True:
        num_rolls += 1
        roll = randint(1, 6)
        if roll == second_roll and is_five:
            return num_rolls
        if roll == first_roll:
            is_five = True
        else:
            is_five = False


# print(dice_roll(5, 6))
# print(dice_roll(5, 5))


sum56 = 0
sum55 = 0
for i in range(10000):
    sum56 += dice_roll(5, 6)
    sum55 += dice_roll(5, 5)
print(sum56, sum55)
