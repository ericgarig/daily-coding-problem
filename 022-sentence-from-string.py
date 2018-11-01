"""
Daily Coding Problem - 2018-10-29.

Given a dictionary of words and a string made up of those words
(no spaces), return the original sentence in a list. If there is more
than one possible reconstruction, return any of them. If there is no
possible reconstruction, then return null.

E.g.:
Given the set of words 'quick', 'brown', 'the', 'fox', and the string
"thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox']

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and
the string "bedbathandbeyond", return either
['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""


def words_from_str(str='', word_list=[]):
    """Given a list of words and a string, return the broken out string."""
    sentence_list = []
    while str:
        found = False
        for i in word_list:
            if str.startswith(i):
                sentence_list.append(i)
                str = str[len(i):]
                found = True
                break
        if not found:
            return None
    return sentence_list


print(words_from_str("thequickbrownfox", ['quick', 'brown', 'the', 'fox']))
print(words_from_str("bedbathandbeyond", ['bed', 'bath', 'bedbath', 'and', 'beyond']))
print(words_from_str("bedbathandbeyond", ['bath', 'bedbath', 'bed', 'and', 'beyond']))
print(words_from_str("bedbathandbeyond", ['bed', 'bathand', 'bath', 'and', 'beyond']))
print(words_from_str("invalidsentence", []))
print(words_from_str("abcd", ['b', 'a', 'c', 'e']))
print(words_from_str("abcd", ['b', 'a', 'c', 'd']))
