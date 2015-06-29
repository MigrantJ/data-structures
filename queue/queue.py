from __future__ import unicode_literals


class Node(object):
    # set default pointer to nonetype
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


# Constructor
class Queue(object):
    def __init__(self):
        self.headNode = None
        self.tailNode = None

    def enqueue(self, value):
        tempnode = Node(value)
        if self.size() == 0:
            self.headNode = tempnode
            self.tailNode = tempnode
        else:
            tempnode.next = self.headNode
            self.headNode = tempnode

    def dequeue(self):
        tempnode = self.headNode
        if self.size() == 0:
            raise LookupError
        returnval = self.tailNode.value
        if tempnode.next is None:
            self.headNode = None
            self.tailNode = None
        else:
            while tempnode.next.next is not None:
                tempnode = tempnode.next
            tempnode.next = None
            self.tailNode = tempnode
        return returnval

    def __repr__(self):
        printstr = "("
        temp_node = self.headNode
        while temp_node is not None:
            if printstr != "(":
                printstr = "{},{}".format(printstr, repr(temp_node.value))
            else:
                printstr += repr(temp_node.value)
            temp_node = temp_node.next
        printstr += ")"
        return printstr

    # Returns size of linked list
    def size(self):
        size = 0
        # sets temporary pointer on current head node
        tempnode = self.headNode
        while tempnode is not None:
            size += 1
            # iterate through head node
            tempnode = tempnode.next
        return size
