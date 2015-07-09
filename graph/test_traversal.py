from graph import Graph
from graph import Node
import pytest


@pytest.fixture()
def temp_nodes():
    n1 = Node('a')
    n2 = Node('b')
    n3 = Node('c')
    n4 = Node('d')
    return [n1, n2, n3, n4]


@pytest.fixture()
def empty_graph():
    return Graph()


@pytest.fixture()
def one_node_graph(temp_nodes, empty_graph):
    empty_graph.add_node(temp_nodes[0])
    return empty_graph


@pytest.fixture()
def linear_graph(temp_nodes, empty_graph):
    prev = None
    for node in temp_nodes:
        empty_graph.add_node(node)
        if prev is not None:
            empty_graph.add_edge(prev, node)
        prev = node
    import pdb; pdb.set_trace()
    return empty_graph


def xtest_edges(graph_nodes, temp_nodes):
    graph_nodes.add_edge(temp_nodes[0], temp_nodes[1])
    graph_nodes.add_edge(temp_nodes[1], temp_nodes[2])
    graph_nodes.add_edge(temp_nodes[2], temp_nodes[3])
    graph_nodes.add_edge(temp_nodes[3], temp_nodes[0])
    graph_nodes.add_edge(temp_nodes[2], temp_nodes[0])
    graph_nodes.add_edge(temp_nodes[1], temp_nodes[0])
    assert graph_nodes.breadth_first_traversal(temp_nodes[0]) is True


def test_one_node_graph(temp_nodes, one_node_graph):
    df = one_node_graph.depth_first_traversal(temp_nodes[0])
    bf = one_node_graph.breadth_first_traversal(temp_nodes[0])
    assert df == [temp_nodes[0]]
    assert bf == [temp_nodes[0]]


def test_linear_graph(temp_nodes, linear_graph):
    df = linear_graph.depth_first_traversal(temp_nodes[0])
    bf = linear_graph.breadth_first_traversal(temp_nodes[0])
    assert df == temp_nodes
    assert bf == temp_nodes
