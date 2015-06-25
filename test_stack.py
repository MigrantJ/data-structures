from __future__ import unicode_literals
import pytest
from stack import Stack

@pytest.fixture()
def empty_stack():
    stack = Stack()
    return stack


@pytest.fixture()
def full_stack():
    stack = Stack([1, 2, 'a', 3, None, 'foobar'])
    return stack


def test_constructor(empty_stack, full_stack):
    assert isinstance(empty_stack, Stack)
    assert isinstance(full_stack, Stack)


def test_pop(empty_stack, full_stack):
    with pytest.raises(LookupError):
        val = empty_stack.pop()

    val = full_stack.pop()
    assert val == 'foobar'
    val = full_stack.pop()
    assert val is None
    val = full_stack.pop()
    assert val == 3


def test_push(empty_stack, full_stack):
    empty_stack.push(None)
    empty_stack.push(1)
    empty_stack.push('two')
    val = empty_stack.pop()
    assert val == 'two'
    val = empty_stack.pop()
    assert val == 1
    full_stack.push(3)
    full_stack.push('four')
    full_stack.push(True)
    val = full_stack.pop()
    assert val is True
    val = full_stack.pop()
    assert val == 'four'
    val = full_stack.pop()
    assert val == 3


def test_other_methods(empty_stack):
    with pytest.raises(AttributeError):
        print(empty_stack.size())
    with pytest.raises(AttributeError):
        print(empty_stack.display())
    with pytest.raises(AttributeError):
        empty_stack.search(1)
    with pytest.raises(AttributeError):
        empty_stack.insert(2)
    with pytest.raises(AttributeError):
        empty_stack.remove(empty_stack.search(1))