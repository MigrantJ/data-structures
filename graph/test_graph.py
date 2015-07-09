# from __future__ import unicode_literals
# import pytest
# from graph import Graph
# from graph import Node


# @pytest.fixture()
# def empty_graph():
#     graph = Graph()
#     return graph


# @pytest.fixture()
# def temp_nodes():
#     n1 = Node('a')
#     n2 = Node('b')
#     n3 = Node(123)
#     return [n1, n2, n3]


# @pytest.fixture()
# def graph_nodes(temp_nodes):
#     graph = Graph()
#     for nodes in temp_nodes:
#         graph.add_node(nodes)
#     return graph


# def test_constructor(empty_graph):
#     assert isinstance(empty_graph, Graph)


# def test_addnode(empty_graph):
#     n1 = Node('a')
#     n2 = Node('b')
#     n3 = Node(123)
#     empty_graph.add_node(n1)
#     empty_graph.add_node(n2)
#     empty_graph.add_node(n3)
#     assert empty_graph.has_node(n1) is True
#     assert empty_graph.has_node(n2) is True
#     assert empty_graph.has_node(123) is not True
#     assert empty_graph.has_node(n3) is True
#     list_nodes = empty_graph.nodes()
#     assert n1 in list_nodes
#     assert n2 in list_nodes
#     assert n3 in list_nodes


# def test_delnode(graph_nodes, temp_nodes):
#     assert graph_nodes.has_node(temp_nodes[0]) is True
#     graph_nodes.del_node(temp_nodes[0])
#     assert graph_nodes.has_node(temp_nodes[0]) is False
#     with pytest.raises(KeyError):
#         graph_nodes.del_node(temp_nodes[0])


# def test_edges(graph_nodes, temp_nodes):
#     assert len(graph_nodes.edges()) == 0
#     graph_nodes.add_edge(temp_nodes[0], temp_nodes[1])
#     assert (temp_nodes[0], temp_nodes[1]) in graph_nodes.edges()
#     assert (temp_nodes[1], temp_nodes[0]) not in graph_nodes.edges()
#     graph_nodes.add_edge(temp_nodes[2], temp_nodes[1])
#     assert (temp_nodes[2], temp_nodes[1]) in graph_nodes.edges()
#     graph_nodes.add_edge(temp_nodes[1], temp_nodes[2])
#     assert (temp_nodes[1], temp_nodes[2]) in graph_nodes.edges()
#     graph_nodes.add_edge(temp_nodes[1], 'b')
#     assert graph_nodes.has_node('b')
#     assert (temp_nodes[1], 'b') in graph_nodes.edges()
#     graph_nodes.del_edge(temp_nodes[1], 'b')
#     assert graph_nodes.has_node('b') is True
#     assert (temp_nodes[1], 'b') not in graph_nodes.edges()
#     with pytest.raises(KeyError):
#         graph_nodes.del_edge(temp_nodes[1], 'b')
#     with pytest.raises(KeyError):
#         graph_nodes.del_edge(temp_nodes[1], 'imaginarynode')


# def test_neighbors(graph_nodes, temp_nodes):
#     graph_nodes.add_edge(temp_nodes[0], temp_nodes[1])
#     graph_nodes.add_edge(temp_nodes[2], temp_nodes[1])
#     graph_nodes.add_edge(temp_nodes[1], temp_nodes[2])
#     graph_nodes.add_edge(temp_nodes[1], 'b')
#     assert temp_nodes[1] in graph_nodes.neighbors(temp_nodes[0])
#     assert temp_nodes[0] not in graph_nodes.neighbors(temp_nodes[1])
#     assert temp_nodes[1] not in graph_nodes.neighbors('b')
#     with pytest.raises(KeyError):
#         graph_nodes.neighbors('imaginarynode')


# def test_adj(graph_nodes, temp_nodes):
#     graph_nodes.add_edge(temp_nodes[0], temp_nodes[1])
#     graph_nodes.add_edge(temp_nodes[2], temp_nodes[1])
#     graph_nodes.add_edge(temp_nodes[1], temp_nodes[2])
#     graph_nodes.add_edge(temp_nodes[1], 'b')
#     assert graph_nodes.adjacent(temp_nodes[0], temp_nodes[1]) is True
#     assert graph_nodes.adjacent(temp_nodes[1], temp_nodes[0]) is False
#     with pytest.raises(KeyError):
#         graph_nodes.adjacent(temp_nodes[0], 'imag node')
