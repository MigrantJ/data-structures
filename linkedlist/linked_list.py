from __future__ import unicode_literals


class Node(object):
    # set default pointer to nonetype
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


# Constructor
class LinkedList(object):
    def __init__(self, values=None):
        self.headNode = None
        if values is not None:
            for value in values:
                self.insert(value)

    # String representation
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
        temp_node = self.headNode
        while temp_node is not None:
            size += 1
            # iterate through head node
            temp_node = temp_node.next
        return size

    # returns a string representation of all values
    def display(self):
        return repr(self)

    # searches to see if value exists, returns node of passed-in value
    def search(self, value):
        iterations = self.size()
        temp_node = self.headNode
        for x in range(0,iterations):
            if temp_node.value == value:
                return temp_node
            temp_node = temp_node.next
        return None

    # insert value at the head of the list
    def insert(self, value):
        temp_node = Node(value,self.headNode)
        self.headNode = temp_node

    # pop the first value
    def pop(self):
        if self.size() == 0:
            raise LookupError
        temp_node = self.headNode
        self.headNode = self.headNode.next
        temp_node.next = None
        return temp_node.value

    # remove node based on  given node
    def remove(self, node):
        temp_node = self.headNode
        temp_node2 = self.headNode.next
        if temp_node == node:
            self.headNode = self.headNode.next
            temp_node.next = None
        else:
            while temp_node2 is not None:
                if temp_node2 == node:
                    temp_node.next = temp_node2.next
                    temp_node2.next = None
                    break
                else:
                    temp_node = temp_node.next
                    temp_node2 = temp_node2.next
            else:
                raise ValueError('node not found')
