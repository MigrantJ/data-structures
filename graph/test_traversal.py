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
def graph_nodes(temp_nodes):
    graph = Graph()
    for nodes in temp_nodes:
        graph.add_node(nodes)
    return graph


def test_edges(graph_nodes, temp_nodes):
    graph_nodes.add_edge(temp_nodes[0], temp_nodes[1])
    graph_nodes.add_edge(temp_nodes[1], temp_nodes[2])
    graph_nodes.add_edge(temp_nodes[2], temp_nodes[3])
    graph_nodes.add_edge(temp_nodes[3], temp_nodes[0])
    graph_nodes.add_edge(temp_nodes[2], temp_nodes[0])
    graph_nodes.add_edge(temp_nodes[1], temp_nodes[0])
    # assert graph_nodes.depth_first_traversal(temp_nodes[0]) is True
    assert graph_nodes.breadth_first_traversal(temp_nodes[0]) is True
