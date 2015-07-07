from __future__ import unicode_literals
import pytest
from graph import Graph

@pytest.fixture()
def empty_graph():
    graph = Graph()
    return graph

@pytest.fixture()
def full_graph():
    graph = Graph()
    graph.add



def test_constructor(empty_graph):
    assert isinstance(empty_graph, Graph)


def nodes
