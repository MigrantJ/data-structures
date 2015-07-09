from __future__ import unicode_literals


def depth_first_traversal(self, start, return_set=[]):
    neighbors = self.neighbors(start).copy()
    temp_node = start
    if temp_node not in return_set:
            return_set.append(temp_node)
    while neighbors:
        temp_node = neighbors.pop()
        if temp_node not in return_set:
            depth_first_traversal(temp_node, return_set)
    return return_set