from __future__ import unicode_literals
from stack import Stack


def paren(str):
    parenStack = Stack(['end'])
    for char in unicode(str):
        if char == '(':
            parenStack.push(1)
        elif char == ')':
            tempchar = parenStack.pop()
            if tempchar == 'end':
                return -1
    returnval = parenStack.pop()
    if returnval == 'end':
        returnval = 0
    return returnval