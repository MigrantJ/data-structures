from functools import total_ordering
from binheap import BinHeap


@total_ordering
class Node(object):
    def __init__(self, priority, val):
        self.priority = priority
        self.val = val

    def __eq__(self, other):
        return self.priority == other.priority

    def __lt__(self, other):
        return self.priority < other.priority


class Priorityq(object):
    def __init__(self):
        self.binheap = BinHeap()

    def insert(self, priority, val):
        new_node = Node(priority, val)
        self.binheap.push(new_node)

    def pop(self):
        return_node = self.binheap.pop()
        return return_node.val

    def peek(self):
        return_node = self.binheap.pop()
        return return_node.val
