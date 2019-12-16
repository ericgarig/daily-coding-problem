"""
Daily Coding Problem - 2019-05-21.

You come across a dictionary of sorted words in a language you've never
seen before. Write a program that returns the correct order of letters
in this language.

For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'],
you should return ['x', 'z', 'w', 'y'].
"""


"""NOTE:
works in specified scenario, needs more testing & refactor.
"""


def solve(arr=[], missing=set()):
    """Sort unknown alphabet."""
    if not arr or (len(arr) == 1 and arr[0][0] == ""):
        return [""]
    if len(arr) == 1:
        return arr[0][0]
    for i in arr:
        for j in list(i):
            missing.add(j)
    missing = list(missing)
    alpha = first_letter_order(arr)
    missing = list_substration(missing, alpha)
    if not missing:
        return alpha
    while missing:
        sub_order = []
        for i in alpha:
            sub_words = [w[1:] for w in arr if i == w[:1]]
            sub_alpha = first_letter_order(sub_words)
            if len(sub_alpha) != len(sub_words):
                sub_order.append(
                    first_letter_order(remove_first_letter(sub_words))
                )
        alpha, missing = insert_letter(alpha, missing, sub_order)
        break
    return alpha


def insert_letter(arr, missing, order_list):
    """Insert letter into alphabet list given an order of letters."""
    for i in missing:
        missing_list = [j for j in order_list if i in j]
        before = len(arr)
        after = 0
        for j in missing_list:
            if i == j[0]:
                before = min(before, arr.index(j[1]))
            elif i == j[1]:
                after = max(after, arr.index(j[0]))
        if before - after == 1:
            arr.insert(after + 1, i)
            missing.remove(i)
    return arr, missing


def list_substration(the_list, remove_these):
    """Remove all items in the first that are also in the 2nd."""
    return [item for item in the_list if item not in remove_these]


def remove_first_letter(arr):
    """Remove the first letter from every word in the array."""
    while True:
        prefix = set()
        new_array = []
        for i in arr:
            prefix.add(i[0])
            new_array.append(i[1:])
        if len(prefix) != 1:
            return arr
        arr = new_array
    return new_array


def first_letter_order(arr):
    """Get the alphabet order based the first letter of words."""
    if len(arr) == 1:
        return [arr[0][0]]
    elif arr[0] == "":
        return [""]
    alpha = []
    for i in arr:
        if i[0] not in alpha:
            alpha.append(i[0])
    return alpha


assert solve(["xww", "wxyz", "wxyw", "ywx", "ywz"]) == ["x", "z", "w", "y"]
# assert solve(["bz", "de", "ee", "aa", "dz"]) == ["b", "d", "z", "e", "a"]
