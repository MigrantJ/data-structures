from __future__ import unicode_literals
import pytest
from queue import Queue

test_values = [
    'a',
    'b',
    'c',
    'd'
]

@pytest.fixture()
def empty_queue():
    queue = Queue()
    return queue

@pytest.fixture()
def full_queue():
    queue = Queue()
    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')
    queue.enqueue('d')
    return queue


def test_constructor(empty_queue):
    assert isinstance(empty_queue, Queue)


def test_dequeue(empty_queue, full_queue):
    with pytest.raises(LookupError):
        val = empty_queue.dequeue()
    assert full_queue.dequeue() == 'a'
    assert full_queue.dequeue() == 'b'
    assert full_queue.dequeue() == 'c'
    assert full_queue.dequeue() == 'd'
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
    assert full_queue.dequeue() == 'a'


def test_size(empty_queue, full_queue):
    assert empty_queue.size() == 0
    assert full_queue.size() == len(test_values)
    empty_queue.enqueue('a thing')
    assert empty_queue.size() == 1
    assert full_queue.dequeue() == 'a'
    assert full_queue.dequeue() == 'b'
    assert full_queue.size() == len(test_values) - 2
