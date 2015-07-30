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

    def _rotatelefttochild(self):
        node = self  # 3
        parent = self.parent  # 5
        child = self.right  # 4
        left = self.right.left  # 4's left child

        parent.left = child
        child.parent = parent

        child.left = node
        node.parent = child

        node.right = left
        if left is not None:
            left.parent = node

    def _rotaterighttochild(self):
        node = self  # 8
        parent = self.parent  # 6
        child = self.left  # 7
        right = self.left.right  # 7's right child

        parent.right = child
        child.parent = parent

        child.right = node
        node.parent = child

        node.left = right
        if right is not None:
            right.parent = node

    def _rotatelefttoparent(self):
        node = self
        parent = self.parent
        left = self.left

        parent.right = left
        if left is not None:
            left.parent = parent

        node.parent = parent.parent
        if node.parent is not None:
            if node.parent.right is parent:
                node.parent.right = node
            else:
                node.parent.left = node

        node.left = parent
        parent.parent = node

    def _rotaterighttoparent(self):
        node = self
        parent = self.parent
        right = self.right

        parent.left = right
        if right is not None:
            right.parent = parent

        node.parent = parent.parent
        if node.parent is not None:
            if node.parent.right is parent:
                node.parent.right = node
            else:
                node.parent.left = node

        node.right = parent
        parent.parent = node


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
        self._rebalance(n.parent)

    def _rebalance(self, root):
        pivot = None
        parent = root.parent
        if root.balance() >= 2:
            # import pdb; pdb.set_trace()
            pivot = root.left
            if pivot.balance() == -1:
                pivot._rotatelefttochild()
                pivot = pivot.parent.parent
                pivot._rotaterighttoparent()
            elif pivot.balance() >= 0:
                pivot._rotaterighttoparent()
        elif root.balance() <= -2:
            # import pdb; pdb.set_trace()
            pivot = root.right
            if pivot.balance() <= 0:
                pivot._rotatelefttoparent()
            elif pivot.balance() == 1:
                pivot._rotaterighttochild()
                pivot = pivot.parent.parent
                pivot._rotatelefttoparent()

        if parent:
            self._rebalance(parent)
        elif pivot:
            self._head = pivot

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
        """find the parent relationship of node and change that parent's child
        to be to_replace
        """
        if node.parent is not None:
            if node.parent.left is node:
                node.parent.left = to_replace
            else:
                node.parent.right = to_replace
            if to_replace is not None:
                to_replace.parent = node.parent
        else:
            self._head = to_replace
            self._head.parent = None

    def delete(self, value):
        """remove a node from the tree and change the hierarchy to maintain
        BST logic
        """
        # see if the node is in the tree at all
        for n in self.in_order():
            if n.value == value:
                del_node = n
                self._size -= 1
                break
        else:
            return None

        parent = del_node.parent

        # if the node to delete has no children
        if del_node.left is None and del_node.right is None:
            self._reparent(del_node)

        # if it has one child, child takes its place
        elif del_node.left is None or del_node.right is None:
            if del_node.left is not None:
                self._reparent(del_node, del_node.left)
            else:
                self._reparent(del_node, del_node.right)

        # if it has two children, promote largest value on left side
        else:
            to_replace = [n for n in self.in_order(del_node.left)][-1]
            if to_replace.left is not None:
                to_replace.left.parent = to_replace.parent
            if to_replace.parent.left is to_replace:
                to_replace.parent.left = to_replace.left
            else:
                to_replace.parent.right = to_replace.left

            self._reparent(del_node, to_replace)
            to_replace.left = del_node.left
            to_replace.right = del_node.right

            if to_replace.left is not None:
                to_replace.left.parent = to_replace
            if to_replace.right is not None:
                to_replace.right.parent = to_replace

        if parent is not None:
            self._rebalance(parent)

        return None

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

    tree = fill_tree([5, 3, 4])
    # tree.delete(6)
    with open('tree_dot.gv', 'w') as fh:
        fh.write(tree.get_dot())
    # t0 = time()
    # worst_case_performance()
    # tpy = time() - t0
    # print "Worst Case Performance {}".format(tpy)
    #
    # t0 = time()
    # best_case_performance()
    # tpy = time() - t0
    # print "Best Case Performance {}".format(tpy)
