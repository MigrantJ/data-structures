# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class BinHeap(object):
    """Implementation of a min binary heap."""
    def __init__(self):
        self.tree = []

    def __repr__(self):
        return repr(self.tree)

    def sort_up(self, c_index):
        p_index = (max(0, c_index - 1)) // 2
        # print("Parent Index: " + str(p_index))
        # print("Child Index: " + str(c_index))

        if self.tree[c_index] < self.tree[p_index]:
            # print("------")
            self.tree[p_index], self.tree[c_index] = self.tree[c_index], self.tree[p_index]
            self.sort_up(p_index)

    def push(self, val):
        self.tree.append(val)
        self.sort_up(len(self.tree) - 1)

    def pop(self):
        pass
