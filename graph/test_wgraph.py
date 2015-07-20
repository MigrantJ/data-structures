from __future__ import unicode_literals
import pytest
from wgraph import Graph
from wgraph import Node

@pytest.fixture()
def empty_graph():
    graph = Graph()
    return graph


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
            empty_graph.add_edge(prev, node, 1)
        prev = node
    return empty_graph


@pytest.fixture()
def circle_graph(temp_nodes, linear_graph):
    linear_graph.add_edge(temp_nodes[3], temp_nodes[0], 1)
    return linear_graph


@pytest.fixture()
def loop_graph(temp_nodes, linear_graph):
    linear_graph.add_edge(temp_nodes[0], temp_nodes[3], 1)
    return linear_graph


@pytest.fixture()
def branch_graph_and_nodes(empty_graph):
    na = Node('a')
    nb = Node('b')
    nc = Node('c')
    nd = Node('d')
    ne = Node('e')
    nf = Node('f')
    ng = Node('g')
    empty_graph.add_edge(na, nb, 1)
    empty_graph.add_edge(na, nc, 1)
    empty_graph.add_edge(nb, nd, 1)
    empty_graph.add_edge(nb, ne, 1)
    empty_graph.add_edge(nb, nf, 1)
    empty_graph.add_edge(nc, nf, 1)
    empty_graph.add_edge(nd, ng, 1)
    return empty_graph, [na, nb, nc, nd, ne, nf, ng]


def test_constructor(empty_graph):
    assert isinstance(empty_graph, Graph)


def test_hasnode(empty_graph):
    n1 = Node('a')
    empty_graph._data = {n1: set()}
    assert empty_graph.has_node(n1)


def test_addnode(empty_graph):
    n1 = Node('a')
    n2 = Node('b')
    n3 = Node(123)
    empty_graph.add_node(n1)
    empty_graph.add_node(n2)
    empty_graph.add_node(n3)
    assert empty_graph.has_node(n1)
    assert empty_graph.has_node(n2)
    assert not empty_graph.has_node(123)
    assert empty_graph.has_node(n3)
    list_nodes = empty_graph.nodes()
    assert n1 in list_nodes
    assert n2 in list_nodes
    assert n3 in list_nodes


def test_delnode(graph_nodes, temp_nodes):
    assert graph_nodes.has_node(temp_nodes[0]) is True
    graph_nodes.del_node(temp_nodes[0])
    assert graph_nodes.has_node(temp_nodes[0]) is False
    with pytest.raises(KeyError):
        graph_nodes.del_node(temp_nodes[0])


def xtest_add_edge(graph_nodes, temp_nodes):
    graph_nodes.add_edge(temp_nodes[0], temp_nodes[1], 1)
    graph_nodes.add_edge(temp_nodes[0], temp_nodes[2], 2)
    edges = graph_nodes.edges()
    n0, edges0 = edges[0]
    n1, edges1 = edges[1]
    n2, edges2 = edges[2]
    assert n1 == temp_nodes[0]
    assert temp_nodes[1] in edges0


def test_edges(graph_nodes, temp_nodes):
    assert len(graph_nodes.edges()) == 0
    graph_nodes.add_edge(temp_nodes[0], temp_nodes[1], 1)
    assert (temp_nodes[0], temp_nodes[1]) in graph_nodes.edges()
    assert (temp_nodes[1], temp_nodes[0]) not in graph_nodes.edges()
    graph_nodes.add_edge(temp_nodes[2], temp_nodes[1], 1)
    assert (temp_nodes[2], temp_nodes[1]) in graph_nodes.edges()
    graph_nodes.add_edge(temp_nodes[1], temp_nodes[2], 1)
    assert (temp_nodes[1], temp_nodes[2]) in graph_nodes.edges()
    graph_nodes.add_edge(temp_nodes[1], 'b', 1)
    assert graph_nodes.has_node('b')
    assert (temp_nodes[1], 'b') in graph_nodes.edges()
    graph_nodes.del_edge(temp_nodes[1], 'b')
    assert graph_nodes.has_node('b') is True
    assert (temp_nodes[1], 'b') not in graph_nodes.edges()
    with pytest.raises(KeyError):
        graph_nodes.del_edge(temp_nodes[1], 'b')
    with pytest.raises(KeyError):
        graph_nodes.del_edge(temp_nodes[1], 'imaginarynode')


def test_neighbors(graph_nodes, temp_nodes):
    graph_nodes.add_edge(temp_nodes[0], temp_nodes[1], 1)
    graph_nodes.add_edge(temp_nodes[2], temp_nodes[1], 1)
    graph_nodes.add_edge(temp_nodes[1], temp_nodes[2], 1)
    graph_nodes.add_edge(temp_nodes[1], 'b', 1)
    assert temp_nodes[1] in graph_nodes.neighbors(temp_nodes[0])
    assert temp_nodes[0] not in graph_nodes.neighbors(temp_nodes[1])
    assert temp_nodes[1] not in graph_nodes.neighbors('b')
    with pytest.raises(KeyError):
        graph_nodes.neighbors('imaginarynode')


def test_adj(graph_nodes, temp_nodes):
    graph_nodes.add_edge(temp_nodes[0], temp_nodes[1], 1)
    graph_nodes.add_edge(temp_nodes[2], temp_nodes[1], 1)
    graph_nodes.add_edge(temp_nodes[1], temp_nodes[2], 1)
    graph_nodes.add_edge(temp_nodes[1], 'b', 1)
    assert graph_nodes.adjacent(temp_nodes[0], temp_nodes[1]) is True
    assert graph_nodes.adjacent(temp_nodes[1], temp_nodes[0]) is False


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


def test_circle_graph(temp_nodes, circle_graph):
    df = circle_graph.depth_first_traversal(temp_nodes[0])
    bf = circle_graph.breadth_first_traversal(temp_nodes[0])
    assert df == temp_nodes
    assert bf == temp_nodes


def test_loop_graph(temp_nodes, loop_graph):
    df = loop_graph.depth_first_traversal(temp_nodes[0])
    assert df[0] == temp_nodes[0]
    assert df[1] in [temp_nodes[1], temp_nodes[3]]
    temp_val_list = [n.value for n in temp_nodes]
    df_val_list = [n.value for n in df]
    assert ''.join(temp_val_list[1:3]) in ''.join(df_val_list)

    bf = loop_graph.breadth_first_traversal(temp_nodes[0])
    assert bf[0] == temp_nodes[0]
    assert bf[-1] == temp_nodes[2]


def test_branch_graph(branch_graph_and_nodes):
    graph, nodes = branch_graph_and_nodes
    df = graph.depth_first_traversal(nodes[0])
    assert df[0] == nodes[0]
    df_str = ''.join([n.value for n in df])
    assert df_str.index('a') < df_str.index('b')
    assert df_str.index('b') < df_str.index('d')
    assert df_str.index('d') < df_str.index('g')

    bf = graph.breadth_first_traversal(nodes[0])
    assert bf[0] == nodes[0]
    assert bf[-1] == nodes[-1]
    bf_str = ''.join([n.value for n in bf])
    assert bf_str.index('a') < bf_str.index('b')
    assert bf_str.index('b') < bf_str.index('d')
    assert bf_str.index('b') < bf_str.index('e')
    assert bf_str.index('b') < bf_str.index('f')
    assert bf_str.index('c') < bf_str.index('d')
    assert bf_str.index('c') < bf_str.index('e')
    assert bf_str.index('c') < bf_str.index('f')
