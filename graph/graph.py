# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Node(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return repr(self.value)


class Graph(object):
    def __init__(self):
        self._data = {}

    def __repr__(self):
        rep = []
        for k, v in self._data.iteritems():
            rep.append('{}: {}'.format(k, v))
        return '\n'.join(rep)

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return [k for k in self._data.iterkeys()]

    def edges(self):
        """Return a list of all edges in the graph. Edges are represented by a
        tuple, with the first item being the origin node and the second item
        being the target.
        """
        edgelist = []
        for node, others in self._data.iteritems():
            for o in others:
                edgelist.append((node, o))
        return edgelist

    def add_node(self, n):
        """Add a new node 'n' to the graph. n must be an instance of Node."""
        self._data.setdefault(n, set())

    def add_edge(self, n1, n2):
        """Add a new edge to the graph connecting n1 to n2. n1 and n2 must be
        instances of Node. If n1 or n2 are not in the graph, they are added.
        """
        if not self.has_node(n1):
            self.add_node(n1)

        if not self.has_node(n2):
            self.add_node(n2)

        self._data[n1].add(n2)

    def del_node(self, n):
        """Delete node n from the graph. If no such node exists, raise
        KeyError.
        """
        for node, e in self._data.iteritems():
            e.discard(n)
        del self._data[n]

    def del_edge(self, n1, n2):
        """Delete the edge connecting n1 to n2. If n1 does not exist in the
        graph, raise KeyError. If n1 is not connected to n2, raise KeyError.
        """
        self._data[n1].remove(n2)

    def has_node(self, n):
        """Return True if node n is in the graph, False if not."""
        return n in self._data

    def neighbors(self, n):
        """Return a list of all nodes connected to n by edges."""
        return self._data[n]

    def adjacent(self, n1, n2):
        """Return True if an edge connects n1 to n2, return False if not.
        If n1 or n2 is not in the graph, raise KeyError.
        """
        if n2 not in self._data:
            raise KeyError
        return n2 in self._data[n1]
