from __future__ import unicode_literals
import pytest
from binheap import BinHeap


@pytest.fixture()
def full_heap():
    fullheap = BinHeap([-1, 20, 25, 20, 5, 87.0, 33, 1046, 11.6, 0, 3, 6])
    return fullheap


@pytest.fixture()
def empty_heap():
    emptyheap = BinHeap()
    return emptyheap


def helper(testHeap):
    for number in range(len(testHeap)):
        try:
            #First Child
            if testHeap[number] > testHeap[(2*number + 1)]:
                return False
            #Second Child
            if testHeap[number] > testHeap[(2*number + 2)]:
                return False
        except IndexError:
            return True


def test_constructor():
    bh = BinHeap([5, 20, 0, 1298, 5.23, 35, 0, 1, 1, -34, 35])
    assert helper(bh)


def test_push(full_heap, empty_heap):
    assert len(empty_heap) == 0
    empty_heap.push(1)
    empty_heap.push(0)
    empty_heap.push(2)
    assert len(empty_heap) == 3
    assert helper(empty_heap)

    assert len(full_heap) == 12
    assert helper(full_heap)
    full_heap.push(0)
    full_heap.push(47)
    full_heap.push(-3)
    full_heap.push(0.0001)
    assert helper(full_heap)


def test_pull(full_heap, empty_heap):
    full_heap.pop()
    assert len(full_heap) == 11
    assert helper(full_heap) is True
    full_heap.pop()
    assert len(full_heap) == 10
    assert helper(full_heap) is True
    empty_heap = BinHeap()
    with pytest.raises(LookupError):
        empty_heap.pop()
    empty_heap.push(2)
    assert empty_heap.pop() == 2
    with pytest.raises(LookupError):
        empty_heap.pop()
