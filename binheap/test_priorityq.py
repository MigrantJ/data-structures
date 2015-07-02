from __future__ import unicode_literals
import pytest
from priorityq import Priorityq


@pytest.fixture()
def empty_q():
    return Priorityq()


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
    empty_q.insert(0, 3)
    empty_q.insert(0, 4)
    empty_q.insert(0, 5)
    assert empty_q.pop() == 0
    assert empty_q.pop() == 1
    assert empty_q.pop() == 2
    assert empty_q.pop() == 3
    assert empty_q.pop() == 4
    assert empty_q.pop() == 5


def test_odd_values(empty_q):
    empty_q.insert(0, None)
    empty_q.insert(1, 'One')
    empty_q.insert(2, [2, 3])
    assert empty_q.pop() is None
    assert empty_q.pop() == 'One'
    assert empty_q.pop() == [2, 3]


def test_full_pop(empty_q):
    # values are the order we expect to receive them in when we pop
    empty_q.insert(3, 3)
    empty_q.insert(0, 0)
    empty_q.insert(2, 2)
    empty_q.insert(10, 6)
    empty_q.insert(3, 4)
    empty_q.insert(5, 5)
    empty_q.insert(0, 1)

    for i in range(0, 7):
        assert empty_q.pop() == i


def test_peek(empty_q):
    empty_q.insert(1, 'hello')
    assert empty_q.peek() == 'hello'
    assert empty_q.peek() == 'hello'


def test_peek_empty(empty_q):
    with pytest.raises(LookupError):
        empty_q.peek()
