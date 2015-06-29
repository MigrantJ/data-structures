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


def test_constructor():
    pass


def test_dequeue():
    pass


def test_enqueue():
    pass


def test_size():
    pass
