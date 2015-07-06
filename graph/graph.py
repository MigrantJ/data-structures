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
        return [k for k in self._data.iterkeys()]

    def edges(self):
        edgelist = []
        for node, others in self._data.iteritems():
            for o in others:
                edgelist.append((node, o))
        return edgelist

    def add_node(self, n):
        self._data[n] = []

    def add_edge(self, n1, n2):
        if not self.has_node(n1):
            self.add_node(n1)

        if not self.has_node(n2):
            self.add_node(n2)

        if n2 not in self._data[n1]:
            self._data[n1].append(n2)

    def del_node(self, n):
        del self._data[n]

    def del_edge(self, n1, n2):
        i = self._data[n1].index(n2)
        del self._data[n1][i]

    def has_node(self, n):
        return n in self._data

    def neighbors(self, n):
        return self._data[n]

    def adjacent(self, n1, n2):
        return n2 in self._data[n1]
