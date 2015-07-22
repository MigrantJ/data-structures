from __future__ import unicode_literals
from queue import Queue
from graph import Node


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
            edgelist.append((node, others))
        return edgelist

    def add_node(self, n):
        """Add a new node 'n' to the graph. n must be an instance of Node."""
        self._data.setdefault(n, {})

    def add_edge(self, n1, n2, weight):
        """Add a new edge to the graph connecting n1 to n2. n1 and n2 must be
        instances of Node. If n1 or n2 are not in the graph, they are added.
        """
        if not self.has_node(n1):
            self.add_node(n1)

        if not self.has_node(n2):
            self.add_node(n2)

        self._data[n1].setdefault(n2, weight)

    def del_node(self, n):
        """Delete node n from the graph. If no such node exists, raise
        KeyError.
        """
        for node, e in self._data.iteritems():
            try:
                del e[n]
            except KeyError:
                continue
        del self._data[n]

    def del_edge(self, n1, n2):
        """Delete the edge connecting n1 to n2. If n1 does not exist in the
        graph, raise KeyError. If n1 is not connected to n2, raise KeyError.
        """
        self._data[n1].pop(n2)

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
        return n2 in self._data[n1]

    def depth_first_traversal(self, start, return_set=None):
        if return_set is None:
            return_set = []
        temp_node = start
        if temp_node not in return_set:
            return_set.append(temp_node)
        for temp_node in self.neighbors(start):
            if temp_node not in return_set:
                self.depth_first_traversal(temp_node, return_set)
        return return_set

    def breadth_first_traversal(self, start, return_set=None):
        if return_set is None:
            return_set = []
        temp_queue = Queue()
        if start not in return_set:
            return_set.append(start)
        for temp_node in self.neighbors(start):
            if temp_node not in return_set:
                return_set.append(temp_node)
                temp_queue.enqueue(temp_node)
        while temp_queue.size() != 0:
            temp_node = temp_queue.dequeue()
            self.breadth_first_traversal(temp_node, return_set)
        return return_set

    def sp_dijkstra(self, start, dest):
        pass

    def sp_bellmanford(self, source, dest, verts=None, edges=None):
        verts = verts or self.nodes()
        edges = edges or self.edges()
        distance = {}
        predecessor = {}

        for v in verts:
            if v is source:
                distance.setdefault(v, 0)
            else:
                distance.setdefault(v, None)

        for i in range(len(verts) - 1):
            for start, d in edges:
                for end, weight in d.items():
                    if distance[end] is None or distance[start] + weight < distance[end]:
                        distance[end] = distance[start] + weight
                        predecessor[end] = start

        current = dest
        path = []
        while current is not source:
            path.append(current)
            current = predecessor[current]
        path.append(source)
        return path[::-1]
