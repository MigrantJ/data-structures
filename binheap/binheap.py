# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class BinHeap(object):
    """Implementation of a min binary heap."""
    def __init__(self):
        self.tree = []

    def __repr__(self):
        print self.tree

    def sort_up(self, index):
        p_index = (index - 1) // 2

        if self.tree[index] < self.tree[p_index]:
            self.tree[p_index], self.tree[index] = self.tree[index], self.tree[p_index]
            self.sort_up(p_index)

    def push(self, val):
        self.tree.append(val)
        self.sort_up(len(self.tree) - 1)

    def pop(self):
        pass
