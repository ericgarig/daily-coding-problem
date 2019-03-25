"""
Daily Coding Problem - 2019-03-19.

Given a list of words, return the shortest unique prefix of each word.

For example, given the list: ['dog', 'cat', 'apple', 'apricot', 'fish'],
return the list ['d','c','app','apr','f'].
"""


def solve(arr):
    """Given a list, return the shortest unique prefix."""
    word_map = {}
    for one_word in arr:
        map_ref = word_map
        for one_char in list(one_word):
            if one_char not in map_ref:
                map_ref[one_char] = {}
            map_ref = map_ref[one_char]
    result = []
    for one_word in arr:
        prefix = one_word[0]
        map_ref = word_map
        for char_index in range(len(one_word)):
            map_ref = map_ref[one_word[char_index]]
            if len(map_ref) > 1:
                prefix = one_word[: (char_index + 2)]
        result.append(prefix)
    return result


assert (solve(["dog", "cat", "apple", "apricot", "fish"])) == [
    "d",
    "c",
    "app",
    "apr",
    "f",
]
