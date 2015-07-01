# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class BinHeap(object):
    """Implementation of a min binary heap."""
    def __init__(self):
        self.tree = []

    def __repr__(self):
        return repr(self.tree)

    def swap(self, i1, i2):
        self.tree[i1], self.tree[i2] = self.tree[i2], self.tree[i1]

    def sort_down(self, p_index):
        lc_index = p_index * 2 + 1
        rc_index = lc_index + 1

        print("Parent Index: " + str(p_index))
        print("Left Child Index: " + str(lc_index))
        print("Right Child Index: " + str(rc_index))
        print("--------")

        try:
            if self.tree[lc_index] <= self.tree[rc_index]:
                self.swap(p_index, lc_index)
                self.sort_down(lc_index)
            elif self.tree[lc_index] > self.tree[rc_index]:
                self.swap(p_index, rc_index)
                self.sort_down(rc_index)
        except IndexError:
            return

    def sort_up(self, c_index):
        p_index = (max(0, c_index - 1)) // 2
        # print("Parent Index: " + str(p_index))
        # print("Child Index: " + str(c_index))

        if self.tree[c_index] < self.tree[p_index]:
            # print("------")
            self.swap(p_index, c_index)
            self.sort_up(p_index)

    def push(self, val):
        self.tree.append(val)
        self.sort_up(len(self.tree) - 1)

    def pop(self):
        last = len(self.tree) - 1
        self.swap(0, last)
        val = self.tree.pop()
        self.sort_down(0)
        return val
