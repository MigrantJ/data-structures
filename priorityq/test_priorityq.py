from __future__ import unicode_literals
import pytest
from priorityq import PriorityQ


@pytest.fixture()
def empty_q():
    return PriorityQ()

@pytest.fixture()
def full_q():
    q = PriorityQ()
    q.push(3)
    q.push(0)
    q.push(2)
    q.push(10)
    q.push(3)
    q.push(5)
    q.push(0)
    return q
