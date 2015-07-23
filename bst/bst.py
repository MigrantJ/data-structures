# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from time import time


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def depth(self):
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        return max(left_depth, right_depth) + 1

    def balance(self):
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        return left_depth - right_depth


class Tree():
    def __init__(self):
        self._head = None
        self._size = 0

    def insert(self, value):
        """insert value into tree. if already present, ignored"""
        n = Node(value)
        if self._head is None:
            self._head = n
            self._size += 1
            return

        parent = None
        direction = 'left'
        current = self._head

        while current is not None:
            if n.value == current.value:
                return
            parent = current

            if n.value < current.value:
                current = current.left
                direction = 'left'
            elif n.value > current.value:
                current = current.right
                direction = 'right'

        if direction == 'left':
            parent.left = n
        else:
            parent.right = n

        self._size += 1

    def contains(self, value):
        """return true if value in tree, false if not"""

        current = self._head
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def size(self):
        """return total number of values stored in tree"""
        return self._size

    def depth(self):
        """return int of total number of tree levels"""
        return self._head.depth() if self._head else 0

    def balance(self):
        """return positive int if more values on left
        negative if more values on right
        0 if balanced
        """
        return self._head.balance() if self._head else 0

if __name__ == '__main__':
    def fill_tree(l):
        out = Tree()
        for n in l:
            out.insert(n)
        return out

    def worst_case_performance():
        return fill_tree([1, 2, 3, 4, 5])

    def best_case_performance():
        return fill_tree([31, 12, 37, 5, 21])

    t0 = time()
    worst_case_performance()
    tpy = time() - t0
    print "Worst Case Performance {}".format(tpy)

    t0 = time()
    best_case_performance()
    tpy = time() - t0
    print "Best Case Performance {}".format(tpy)
