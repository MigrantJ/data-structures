# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class DLNode(object):
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class DLList(object):
    def __init__(self, iterable=None):
        self.head_node = None
        self.tail_node = None
        if iterable:
            for val in iterable:
                self.append(val)

    def __repr__(self):
        current = self.head_node
        accum = []
        while current is not None:
            accum.append(unicode(current.value))
            current = current.next
        return ' | '.join(accum)

    def insert(self, val):
        node = DLNode(val, next=self.head_node)
        if self.head_node:
            self.head_node.prev = node
        else:
            self.tail_node = node
        self.head_node = node

    def append(self, val):
        node = DLNode(val, prev=self.tail_node)
        if self.tail_node:
            self.tail_node.next = node
        else:
            self.head_node = node
        self.tail_node = node

    def pop(self):
        if not self.head_node:
            raise LookupError('List is empty')
        temp = self.head_node
        self.head_node = self.head_node.next
        self.head_node.prev = None
        return temp.value

    def shift(self):
        if not self.tail_node:
            raise LookupError('List is empty')
        temp = self.tail_node
        self.tail_node = self.tail_node.prev
        self.tail_node.next = None
        return temp.value

    def remove(self, val):
        current = self.head_node
        while current is not None:
            if current.value == val:
                if current is self.head_node:
                    self.pop()
                elif current is self.tail_node:
                    self.shift()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                break
            current = current.next
        else:
            raise ValueError('{} not found'.format(val))
