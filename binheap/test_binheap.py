from __future__ import unicode_literals
import pytest
from binheap import Binheap

list1 = [2, 20, 25, 20, 5, 87, 33, 1046, 11, 0, 3, 6]


def test_push():
    testHeap = Binheap()
    for number in list1:
        testHeap.push(list1[number])
    assert len(testHeap) == 12
    for number in (len(testHeap)/2):
        assert Binheap[number] < Binheap[(2*number + 1)]
        assert Binheap[number] < Binheap[(2*number + 1)]

