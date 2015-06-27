from __future__ import unicode_literals
from stack.stack import Stack


def parens(string):
    """Return an integer representing whether all open parentheses are closed
    in order in the provided input.

    Args:
        string (unicode): The string to search through for parens.

    Returns:
        int: Value represents whether parens are matched:
            1: There are open parens that are not closed.
            0: There are an equal number of matched open and close parens.
            -1: There is a closed paren before a matching open paren.
    """

    stack = Stack([-1, 0])
    # ensure input is proper type before iterating
    for c in unicode(string):
        if c == '(':
            stack.push(1)
        elif c == ')':
            if stack.pop() == 0:
                # this is a 'broken' string
                break

    return stack.pop()
