# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Node(object):
    def __init__(self, value):
        self.value = value


class Graph(object):
    def __init__(self):
        self._data = {}

    def nodes(self):
        pass

    def edges(self):
        pass

    def add_node(self, value):
        pass

    def add_edge(self, n1, n2):
        pass

    def del_node(self, n):
        pass

    def del_edge(self, n1, n2):
        pass

    def has_node(self, n):
        pass

    def neighbors(self, n):
        pass

    def adjacent(self, n1, n2):
        pass
