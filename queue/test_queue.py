from __future__ import unicode_literals
import pytest
from queue import Queue

test_values = [
    1,
    None,
    'two',
    [3, 4, 5]
]

@pytest.fixture()
def empty_queue():
    queue = Queue()
    return queue

@pytest.fixture()
def full_queue():
    queue = Queue()
    for val in test_values:
        queue.enqueue(val)
    return queue


def test_constructor(empty_queue):
    assert isinstance(empty_queue, Queue)


def test_dequeue(empty_queue, full_queue):
    with pytest.raises(LookupError):
        val = empty_queue.dequeue()
    for val in test_values:
        assert full_queue.dequeue() == val
    with pytest.raises(LookupError):
        val = full_queue.dequeue()


def test_enqueue(empty_queue, full_queue):
    empty_queue.enqueue(True)
    assert empty_queue.dequeue() is True
    empty_queue.enqueue(55)
    empty_queue.enqueue('test')
    assert empty_queue.dequeue() == 55
    assert empty_queue.dequeue() == 'test'
    with pytest.raises(LookupError):
        val = empty_queue.dequeue()
    full_queue.enqueue(6)
    assert full_queue.dequeue() == test_values[0]


def test_size(empty_queue, full_queue):
    assert empty_queue.size() == 0
    assert full_queue.size() == len(test_values)
    empty_queue.enqueue('a thing')
    assert empty_queue.size() == 1
    assert full_queue.dequeue() == test_values[0]
    assert full_queue.dequeue() == test_values[1]
    assert full_queue.size() == len(test_values) - 2
