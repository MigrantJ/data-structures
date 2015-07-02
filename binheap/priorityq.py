from functools import total_ordering
from binheap import BinHeap


@total_ordering
class Node(object):
    def __init__(self, priority, val, order):
        self.priority = priority
        self.val = val
        self.order = order

    def __repr__(self):
        return 'Pri: ' + repr(self.priority) + ' Val: ' + repr(self.val)

    def __eq__(self, other):
        if self.priority == other.priority:
            return self.order == other.order

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.order < other.order
        else:
            return self.priority < other.priority


class Priorityq(object):
    def __init__(self):
        self.binheap = BinHeap()
        self._count = 0

    def insert(self, priority, val):
        new_node = Node(priority, val, self._count)
        self.binheap.push(new_node)
        self._count += 1

    def pop(self):
        return_node = self.binheap.pop()
        return return_node.val

    def peek(self):
        return self.binheap[0]
