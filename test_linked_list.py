import pytest
from linked_list import LinkedList
list1 = LinkedList([1,2,3,4,5,6,7,8])

def test_const():
    assert list1.headNode != None
    assert list1.headNode.value == 8
    assert list1.headNode.next.value == 7

def test_size():
    assert list1.size() == 8

def test_display():
    assert list1.display() == "(8,7,6,5,4,3,2,1)"

def test_search():
    assert list1.search(3) != None
    assert list1.search(2) != None
    assert list1.search(50) == None

def test_insert():
    assert list1.size() == 8
    list1.insert(5)
    assert list1.display() == "(5,8,7,6,5,4,3,2,1)"
    assert list1.size() == 9

def test_pop():
    assert list1.pop() == 5
    assert list1.size() == 8
    assert list1.display() == "(8,7,6,5,4,3,2,1)"
    assert list1.pop() == 8
    assert list1.size() == 7
    assert list1.display() == "(7,6,5,4,3,2,1)"

def test_remove():
    tempNode = list1.search(1)
    assert list1.remove(tempNode)
    assert list1.search(1) == None
    assert list1.size() ==  6
    assert list1.display() == "(7,6,5,4,3,2)"
    tempNode = list1.search(7)
    assert list1.remove(tempNode)
    assert list1.search(7) == None
    assert list1.size() ==  5
    assert list1.display() == "(6,5,4,3,2)"
    tempNode = list1.search(4)
    assert list1.remove(tempNode)
    assert list1.search(4) == None
    assert list1.size() ==  4
    assert list1.display() == "(6,5,3,2)"
    tempNode = list1.search(7)
    assert list1.remove(tempNode)
    assert list1.search(7) == None
    assert list1.size() ==  5
    assert list1.display() == "(6,5,4,3,2)"


