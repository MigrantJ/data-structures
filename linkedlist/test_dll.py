from __future__ import unicode_literals
import pytest
from dl_list import DLList
from dl_list import Node

test_values = [
    1,
    None,
    'two',
    [3, 4, 5]
]

@pytest.fixture()
def empty_DLList():
    DLList = DLList()
    return DLList

@pytest.fixture()
def full_DLList():
    DLList = DLList(test_values)
    return DLList


def test_constructor(empty_DLList, full_DLList):
    assert isinstance(empty_DLList, full_DLList)
    thead_node = full_DLList.head_node
    ttail_node = full_DLList.tail_node
    fstring = [thead_node.value]
    bstring = [ttail_node.value]
    while thead_node.next != None and ttail_node.prev != None:
        if thead_node.next != None:
            thead_node = thead_node.next
            fstring.append(thead_node.value)
        if ttail_node.prev != None:
            ttail_node = ttail_node.prev
            bstring.append(ttail_node.value)
    assert fstring == bstring[::-1]
    assert fstring == test_values


def test_insert(empty_DLList, full_DLList):
    empty_DLList.insert('b')
    full_DLList.insert('b')
    thead_node = full_DLList.head_node
    ttail_node = full_DLList.tail_node
    fstring = ['b']
    bstring = ['b']
    while thead_node.next != None and ttail_node.prev != None:
        if thead_node.next != None:
            thead_node = thead_node.next
            fstring.append(thead_node.value)
        if ttail_node.prev != None:
            ttail_node = ttail_node.prev
            bstring.append(ttail_node.value)
    assert fstring == bstring[::-1]
    assert fstring[0] == b