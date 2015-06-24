from __future__ import unicode_literals

class Node(object):
    #set default pointer to nonetype
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

#Constructor
class LinkedList(object):
    def __init__(self, values):
        self.headNode = None
        for value in values:
            tempNode = Node(value, self.headNode)
            self.headNode = tempNode

    #Returns size of linked list
    def size(self):
        size = 0
        #sets temporary pointer on current head node
        tempNode = self.headNode
        while tempNode != None:
            size += 1
            #iterate through head node
            tempNode = tempNode.next
        return size



