"""
Daily Coding Problem - 2018-11-03.

Given a string of round, curly, and square open and closing brackets,
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""


def is_match(test_str):
    """Given a test string, determine if the brackets are balanced."""
    bracket_stack = []
    for i in test_str:
        if i == '(' or i == '{' or i == '[':
            bracket_stack.append(i)
        elif not bracket_stack:
            return False
        else:
            last_e = bracket_stack.pop()
            if last_e == '(' and i == ')':
                continue
            elif last_e == '{' and i == '}':
                continue
            elif last_e == '[' and i == ']':
                continue
            else:
                return False
    if bracket_stack:
        return False
    return True


print(is_match('([])[]({})'))    # True
print(is_match('([)]'))    # False
print(is_match('((()'))    # False
