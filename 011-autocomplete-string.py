"""
Daily Coding Problem - 2018-10-18.

Implement an autocomplete system. That is, given a query string s and a
set of all possible query strings, return all strings in the set that
have s as a prefix.

For example, given the query string de and the set of strings:
[dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data
structure to speed up queries.
"""


def autocomplete_readable(s, possible_list):
    """Provide autocomplete options for the specified string."""
    return [i for i in possible_list if i.startswith(s)]


def autocomplete_faster(s, possible_list):
    """Faster way of testing if an item starts with string s."""
    return [i for i in possible_list if i[:len(s)] == s]


print(autocomplete_readable('de', ['dog', 'deer', 'deal']))    # [deer, deal]
print(autocomplete_faster('de', ['dog', 'deer', 'deal']))    # [deer, deal]
