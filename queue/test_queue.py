from __future__ import unicode_literals
import pytest
from queue import Queue

@pytest.fixture()
def empty_queue():
    queue = Queue()
    return queue

@pytest.fixture()
def full_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(None)
    queue.enqueue('two')
    queue.enqueue([3, 4, 5])


def test_constructor(empty_queue):
    assert isinstance(empty_queue, Queue)


def test_dequeue(empty_queue, full_queue):
    with pytest.raises(LookupError):
        val = empty_queue.dequeue()
    assert full_queue.dequeue() == 1
    assert full_queue.dequeue() is None
    assert full_queue.dequeue() == 'two'
    assert full_queue.dequeue() == [3, 4, 5]
    with pytest.raises(LookupError):
        val = full_queue.dequeue()


def test_enqueue():
    pass


def test_size():
    pass
