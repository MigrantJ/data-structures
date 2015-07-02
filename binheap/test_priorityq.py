from __future__ import unicode_literals
import pytest
from priorityq import Priorityq


@pytest.fixture()
def empty_q():
    return Priorityq()


@pytest.fixture()
def full_q():
    q = Priorityq()
    # values are the order we expect to receive them in when we pop
    q.insert(3, 3)
    q.insert(0, 0)
    q.insert(2, 2)
    q.insert(10, 6)
    q.insert(3, 4)
    q.insert(5, 5)
    q.insert(0, 1)
    return q


def test_pop_empty(empty_q):
    with pytest.raises(LookupError):
        empty_q.pop()


def test_insert_and_pop_once(empty_q):
    empty_q.insert(1, 1)
    assert empty_q.pop() == 1
    empty_q.insert(0, 2)
    assert empty_q.pop() == 2


def test_priority(empty_q):
    empty_q.insert(100, 0)
    empty_q.insert(1, 2)
    assert empty_q.pop() == 2


def test_equal_priority(empty_q):
    empty_q.insert(0, 0)
    empty_q.insert(0, 1)
    empty_q.insert(0, 2)
    assert empty_q.pop() == 0
    assert empty_q.pop() == 1
    assert empty_q.pop() == 2


def test_odd_values(empty_q):
    empty_q.insert(0, None)
    empty_q.insert(1, 'One')
    empty_q.insert(2, [2, 3])
    assert empty_q.pop() is None
    assert empty_q.pop() == 'One'
    assert empty_q.pop() == [2, 3]
