"""
Daily Coding Problem - 2018-12-10.

Given a 2D matrix of characters and a target word, write a function that
returns whether the word can be found in the matrix by going
left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

and the target word 'FOAM', you should return true, since it's the
leftmost column. Similarly, given the target word 'MASS', you should
return true, since it's the last row.
"""


def target_word(arr, word):
    """Determine if word is in an array ( L->R, U->D)."""
    for row in arr:
        if word in ''.join(row):
            return True
    for i in range(len(arr[0])):
        one_col = []
        for row in range(len(arr)):
            one_col.append(arr[row][i])
        if word in ''.join(one_col):
            return True
    return False


arr = [['F', 'A', 'C', 'I'],
       ['O', 'B', 'Q', 'P'],
       ['A', 'N', 'O', 'B'],
       ['M', 'A', 'S', 'S']]
print(target_word(arr, 'FOAM'))    # True
print(target_word(arr, 'MASS'))    # True
