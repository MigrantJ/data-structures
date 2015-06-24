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

    #String representation
    def __repr__(self):
        printstr = "("
        tempNode = self.headNode
        while tempNode != None:
            if printstr != "(":
                printstr = "{},{}".format(printstr, tempNode.value)
            else:
                printstr += str(tempNode.value)
            tempNode = tempNode.next
        printstr += ")"
        return printstr

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

    #returns a string representation of all values
    def display(self):
         return str(self)

    #searches to see if value exists, returns node of passed-in value
    def search(self, value):
        iterations = self.size()
        tempNode = self.headNode
        for x in range(0,iterations):
            if tempNode.value == value:
                return tempNode
            tempNode = tempNode.next
        return None

