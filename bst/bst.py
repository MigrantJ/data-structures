# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from time import time
from queue import Queue
import random


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return 'Node: ' + str(self.value)

    def depth(self):
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        return max(left_depth, right_depth) + 1

    def balance(self):
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        return left_depth - right_depth

    def _get_dot(self):
        """recursively prepare a dot graph entry for this node."""
        if self.left is not None:
            yield "\t%s -> %s;" % (self.value, self.left.value)
            for i in self.left._get_dot():
                yield i
        elif self.right is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)
        if self.right is not None:
            yield "\t%s -> %s;" % (self.value, self.right.value)
            for i in self.right._get_dot():
                yield i
        elif self.left is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)


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
        n.parent = parent

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

    def _reparent(self, node, to_replace=None):
        if node.parent is not None:
            if node.parent.left is node:
                node.parent.left = to_replace
            else:
                node.parent.right = to_replace

    def delete(self, value):
        for n in self.in_order():
            if n.value == value:
                del_node = n
                self._size -= 1
                break
        else:
            return None

        # IF NO CHILDREN
        if del_node.left is None and del_node.right is None:
            self._reparent(del_node)

        # IF ONE CHILD
        elif del_node.left is None or del_node.right is None:
            if del_node.left is not None:
                self._reparent(del_node, del_node.left)
            else:
                self._reparent(del_node, del_node.right)

        # IF TWO CHILDREN
        else:
            to_replace = [n for n in self.in_order(del_node.left)][-1]
            to_replace.left.parent = to_replace.parent
            if to_replace.parent.left is to_replace:
                to_replace.parent.left = to_replace.left
            else:
                to_replace.parent.right = to_replace.left

            self._replace(del_node, to_replace)
            to_replace.left = del_node.left
            to_replace.right = del_node.right

    def in_order(self, node=None):
        node = node or self._head
        if node.left is not None:
            for n in self.in_order(node.left):
                yield n
        yield node
        if node.right is not None:
            for n in self.in_order(node.right):
                yield n

    def pre_order(self, node=None):
        node = node or self._head
        yield node
        if node.left is not None:
            for n in self.pre_order(node.left):
                yield n
        if node.right is not None:
            for n in self.pre_order(node.right):
                yield n

    def post_order(self, node=None):
        node = node or self._head
        if node.left is not None:
            for n in self.post_order(node.left):
                yield n
        if node.right is not None:
            for n in self.post_order(node.right):
                yield n
        yield node

    def breadth_first(self):
        q = Queue()
        q.enqueue(self._head)
        try:
            while True:
                node = q.dequeue()
                yield node
                if node.left is not None:
                    q.enqueue(node.left)
                if node.right is not None:
                    q.enqueue(node.right)
        except LookupError:
            pass

    def get_dot(self):
        """return the tree with root 'self' as a dot graph for visualization"""
        return "digraph G{\n%s}" % ("" if self._head.value is None else (
            "\t%s;\n%s\n" % (
                self._head.value,
                "\n".join(self._head._get_dot())
            )
        ))


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

    tree = fill_tree([8, 10, 3, 16, 14, 47, 13])
    tree.delete(16)
    with open('tree_dot.gv', 'w') as fh:
        fh.write(tree.get_dot())
    t0 = time()
    worst_case_performance()
    tpy = time() - t0
    print "Worst Case Performance {}".format(tpy)

    t0 = time()
    best_case_performance()
    tpy = time() - t0
    print "Best Case Performance {}".format(tpy)
