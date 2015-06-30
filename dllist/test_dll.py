from __future__ import unicode_literals
import pytest
from dl_list import DLList

test_values = [
    1,
    None,
    1,
    'two',
    'two',
    [3, 4, 5]
]

@pytest.fixture()
def empty_dllist():
    dl = DLList()
    return dl

@pytest.fixture()
def full_dllist():
    dl = DLList(test_values)
    return dl


def test_constructor(empty_dllist, full_dllist):
    assert isinstance(empty_dllist, DLList)
    thead_node = full_dllist.head_node
    ttail_node = full_dllist.tail_node
    fstring = []
    bstring = []
    if thead_node is not None:
        fstring.append(thead_node.value)
    if thead_node is not None:
        bstring.append(ttail_node.value)
    if thead_node is not None and thead_node is not None:
        while thead_node.next is not None and ttail_node.prev is not None:
            if thead_node.next is not None:
                thead_node = thead_node.next
                fstring.append(thead_node.value)
            if ttail_node.prev is not None:
                ttail_node = ttail_node.prev
                bstring.append(ttail_node.value)
    assert fstring == bstring[::-1]
    assert fstring == test_values


def test_insert(empty_dllist, full_dllist):
    empty_dllist.insert('b')
    full_dllist.insert('b')
    thead_node = full_dllist.head_node
    ttail_node = full_dllist.tail_node
    fstring = [thead_node.value]
    bstring = [ttail_node.value]
    while thead_node.next is not None and ttail_node.prev is not None:
        if thead_node.next is not None:
            thead_node = thead_node.next
            fstring.append(thead_node.value)
        if ttail_node.prev is not None:
            ttail_node = ttail_node.prev
            bstring.append(ttail_node.value)
    assert fstring == bstring[::-1]
    assert fstring[0] == 'b'
    with pytest.raises(TypeError):
        empty_dllist.insert()
    with pytest.raises(TypeError):
        full_dllist.insert()


def test_append(empty_dllist, full_dllist):
    empty_dllist.append(True)
    full_dllist.append(False)
    thead_node = full_dllist.head_node
    ttail_node = full_dllist.tail_node
    fstring = [thead_node.value]
    bstring = [ttail_node.value]
    while thead_node.next is not None and ttail_node.prev is not None:
        if thead_node.next != None:
            thead_node = thead_node.next
            fstring.append(thead_node.value)
        if ttail_node.prev != None:
            ttail_node = ttail_node.prev
            bstring.append(ttail_node.value)
    assert fstring == bstring[::-1]
    assert fstring.pop() is False
    with pytest.raises(TypeError):
        empty_dllist.append()
    with pytest.raises(TypeError):
        full_dllist.append()


def test_pop(empty_dllist, full_dllist):
    with pytest.raises(LookupError):
        empty_dllist.pop()
    tempvar = full_dllist.pop()
    assert tempvar == 1
    thead_node = full_dllist.head_node
    ttail_node = full_dllist.tail_node
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


def test_shift(empty_dllist, full_dllist):
    with pytest.raises(LookupError):
        empty_dllist.shift()
    tempvar = full_dllist.shift()
    assert tempvar == [3,4,5]
    thead_node = full_dllist.head_node
    ttail_node = full_dllist.tail_node
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


def test_remove(empty_dllist, full_dllist):
    full_dllist.remove(1)
    with pytest.raises(ValueError):
        full_dllist.remove('1')
    thead_node = full_dllist.head_node
    ttail_node = full_dllist.tail_node
    fstring = [thead_node.value]
    bstring = [ttail_node.value]
    while thead_node.next is not None and ttail_node.prev is not None:
        if thead_node.next is not None:
            thead_node = thead_node.next
            fstring.append(thead_node.value)
        if ttail_node.prev is not None:
            ttail_node = ttail_node.prev
            bstring.append(ttail_node.value)
    assert fstring == bstring[::-1]
    assert fstring == [None, 1, 'two', 'two', [3,4,5]]
