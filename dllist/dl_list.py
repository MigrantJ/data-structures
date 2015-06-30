# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class DLNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DLList(object):
    def __init__(self):
        self.head_node = None

    def insert(self, val):
        pass

    def append(self, val):
        pass

    def pop(self):
        pass

    def shift(self):
        pass

    def remove(self, val):
        pass
