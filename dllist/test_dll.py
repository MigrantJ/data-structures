from __future__ import unicode_literals
import pytest
from dl_list import DLList
from dl_list import DLNode

test_values = [
    1,
    None,
    1,
    'two',
    'two',
    [3, 4, 5]
]

@pytest.fixture()
def empty_DLList():
    testDLList = DLList()
    return testDLList

@pytest.fixture()
def full_DLList():
    testDLList = DLList(test_values)
    return testDLList


def test_constructor(empty_DLList, full_DLList):
    assert isinstance(empty_DLList, DLList)
    thead_node = full_DLList.head_node
    ttail_node = full_DLList.tail_node
    fstring = []
    bstring = []
    if thead_node != None:
        fstring.append(thead_node.value)
    if thead_node != None:
        bstring.append(ttail_node.value)
    if thead_node != None and thead_node != None:
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
    assert fstring[0] == 'b'
    with pytest.raises(TypeError):
        empty_DLList.insert()
    with pytest.raises(TypeError):
        full_DLList.insert()

def test_append(empty_DLList, full_DLList):
    empty_DLList.append(True)
    full_DLList.append(False)
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
    assert fstring.pop() == False
    with pytest.raises(TypeError):
        empty_DLList.append()
    with pytest.raises(TypeError):
        full_DLList.append()


def test_pop(empty_DLList, full_DLList):
    with pytest.raises(LookupError):
        empty_DLList.pop()
    tempvar = full_DLList.pop()
    assert tempvar == 1
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


def test_shift(empty_DLList, full_DLList):
    with pytest.raises(LookupError):
        empty_DLList.shift()
    tempvar = full_DLList.shift()
    assert tempvar == [3,4,5]
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


def test_remove(empty_DLList, full_DLList):
    full_DLList.remove(1)
    with pytest.raises(ValueError):
        full_DLList.remove('1')
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
    assert fstring == [None, 1, 'two', 'two', [3,4,5]]
