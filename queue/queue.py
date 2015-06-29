from __future__ import unicode_literals


class Node(object):
    # set default pointer to nonetype
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


# Constructor
class Queue(object):
    def __init__(self, values=None):
        self.headNode = None
        self.tailNode = None

    def enqueue(self, value):
        tempNode = Node(value)
        if self.size() == 0:
            self.headNode = tempNode
            self.tailNode = tempNode
        else:
            self.tailNode.next = tempNode
            self.tailNode = tempNode

    def dequeue(self):
        tempNode = self.headNode
        if self.size() == 0:
            raise LookupError
        while (tempNode.next != None):
            tempNode = tempNode.next
        returnVal = self.tailNode.value
        tempNode.next = None
        self.tailNode = tempNode
        return returnVal

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
        tempNode = self.headNode
        while tempNode is not None:
            size += 1
            # iterate through head node
            tempNode = tempNode.next
        return size


