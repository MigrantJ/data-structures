from __future__ import unicode_literals
import pytest
from stack import Stack

@pytest.fixture()
def empty_stack():
    stack = Stack()
    return stack


@pytest.fixture()
def full_stack():
    stack = Stack([1, 2, 3, 'a', 'foobar', None])
    return stack


def test_constructor(empty_stack, full_stack):
    assert isinstance(empty_stack, Stack)
    assert isinstance(full_stack, Stack)


def test_push():
    pass


def test_pop():
    pass