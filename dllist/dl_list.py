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
            temp = self.head_node
            temp.prev = node
            node.next = temp
        else:
            self.tail_node = node
        self.head_node = node

    def append(self, val):
        node = DLNode(val, prev=self.tail_node)
        if self.tail_node:
            temp = self.tail_node
            temp.next = node
            node.prev = temp
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
                break
            current = current.next
        else:
            raise ValueError('{} not found'.format(val))
        return current.value
