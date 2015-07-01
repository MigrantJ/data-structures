# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class BinHeap(object):
    """Implementation of a min binary heap."""
    def __init__(self, iterable=None):
        self.tree = []
        if iterable is not None:
            for val in iterable:
                self.push(val)

    def __repr__(self):
        return repr(self.tree)

    def __len__(self):
        return len(self.tree)

    def __iter__(self):
        for val in self.tree:
            yield val

    def __getitem__(self, item):
        return self.tree[item]

    def swap(self, i1, i2):
        self.tree[i1], self.tree[i2] = self.tree[i2], self.tree[i1]

    def sort_down(self, p_index):
        try:
            p_val = self.tree[p_index]
            lc_index = p_index * 2 + 1
            rc_index = lc_index + 1

            lc_val = self.tree[lc_index]
            try:
                rc_val = self.tree[rc_index]
            except IndexError:
                if lc_val < p_val:
                    self.swap(p_index, lc_index)
            else:
                if lc_val < p_val and lc_val <= rc_val:
                    self.swap(p_index, lc_index)
                    self.sort_down(lc_index)
                elif rc_val < p_val and lc_val > rc_val:
                    self.swap(p_index, rc_index)
                    self.sort_down(rc_index)
        except IndexError:
            pass
        return

    def sort_up(self, c_index):
        p_index = (max(0, c_index - 1)) // 2

        if self.tree[c_index] < self.tree[p_index]:
            self.swap(p_index, c_index)
            self.sort_up(p_index)

    def push(self, val):
        self.tree.append(val)
        self.sort_up(len(self.tree) - 1)

    def pop(self):
        last = len(self.tree) - 1
        if last == -1:
            raise LookupError('Empty binheap')
        self.swap(0, last)
        val = self.tree.pop()
        self.sort_down(0)
        return val
