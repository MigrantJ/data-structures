# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class DLNode(object):
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class DLList(object):
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def insert(self, val):
        node = DLNode(val, self.head_node)
        if self.head_node:
            temp = self.head_node
            temp.prev = node

        self.head_node = node

    def append(self, val):
        pass

    def pop(self):
        pass

    def shift(self):
        pass

    def remove(self, val):
        pass
