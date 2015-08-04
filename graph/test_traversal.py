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
    return empty_graph


@pytest.fixture()
def circle_graph(temp_nodes, linear_graph):
    linear_graph.add_edge(temp_nodes[3], temp_nodes[0])
    return linear_graph


@pytest.fixture()
def loop_graph(temp_nodes, linear_graph):
    linear_graph.add_edge(temp_nodes[0], temp_nodes[3])
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
    empty_graph.add_edge(na, nb)
    empty_graph.add_edge(na, nc)
    empty_graph.add_edge(nb, nd)
    empty_graph.add_edge(nb, ne)
    empty_graph.add_edge(nb, nf)
    empty_graph.add_edge(nc, nf)
    empty_graph.add_edge(nd, ng)
    return empty_graph, [na, nb, nc, nd, ne, nf, ng]


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
