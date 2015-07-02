from __future__ import unicode_literals

import pytest

from binheap.priorityq import PriorityQ


@pytest.fixture()
def empty_q():
    return PriorityQ()


@pytest.fixture()
def full_q():
    q = PriorityQ()
    # values are the order we expect to receive them in when we pop
    q.push(3, 3)
    q.push(0, 0)
    q.push(2, 2)
    q.push(6, 10)
    q.push(4, 3)
    q.push(5, 5)
    q.push(1, 0)
    return q


def test_pop_empty(empty_q):
    with pytest.raises(LookupError):
        empty_q.pop()


def test_pop_full(full_q):
    for i in xrange(0, 7):
        assert full_q.pop() == i
