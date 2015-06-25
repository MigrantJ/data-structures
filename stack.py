from __future__ import unicode_literals
from linked_list import LinkedList


class Stack(object):
    def __init__(self, iterable=None):
        self.data = LinkedList(iterable) if iterable else LinkedList()

    def pop(self):
        return self.data.pop()

    def push(self, value):
        self.data.insert(value)