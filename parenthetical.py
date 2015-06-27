from __future__ import unicode_literals
from stack.stack import Stack


def parens(string):
    stack = Stack(str(string)[::-1])
    balance = 0
    while True:
        try:
            c = stack.pop()
        except LookupError:
            break

        if c == '(':
            balance += 1
        elif c == ')':
            balance -= 1

        if balance < 0:
            break
    return min(balance, 1)
