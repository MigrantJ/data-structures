from __future__ import unicode_literals
import pytest
from linked_list import LinkedList

list1 = LinkedList([1, 2, 3, 4, 5, 6, 7, 8])


def test_const():
    assert list1.headNode is not None
    assert list1.headNode.value == 8
    assert list1.headNode.next.value == 7


def test_size():
    assert list1.size() == 8


def test_display():
    assert list1.display() == "(8,7,6,5,4,3,2,1)"


def test_search():
    assert list1.search(3) is not None
    assert list1.search(2) is not None
    assert list1.search(50) is None


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
    tempnode = list1.search(1)
    list1.remove(tempnode)
    assert list1.search(1) is None
    assert list1.size() == 6
    assert list1.display() == "(7,6,5,4,3,2)"
    tempnode = list1.search(7)
    list1.remove(tempnode)
    assert list1.search(7) is None
    assert list1.size() == 5
    assert list1.display() == "(6,5,4,3,2)"
    tempnode = list1.search(4)
    list1.remove(tempnode)
    assert list1.search(4) is None
    assert list1.size() == 4
    assert list1.display() == "(6,5,3,2)"
    tempnode = list1.search(7)
    with pytest.raises(ValueError):
        list1.remove(tempnode)
    assert list1.search(7) is None
    assert list1.size() == 4
    assert list1.display() == "(6,5,3,2)"
