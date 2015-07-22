class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree():
    def __init__(self):
        self._head = None
        self._size = 0
        self._depth = 0
        self._balance = 0

    def insert(self, value):
        # insert value into tree. if already present, ignored
        n = Node(value)
        if self._head is None:
            self._head = n
            self._size += 1
            self._depth += 1
            return

        parent = None
        direction = 'left'
        current = self._head
        depth = 1

        if value < self._head.value:
            self._balance += 1
        elif value > self._head.value:
            self._balance -= 1

        while current is not None:
            parent = current
            if n.value < current.value:
                current = current.left
                direction = 'left'
            elif n.value > current.value:
                current = current.right
                direction = 'right'
            else:
                return
            depth += 1

        if depth > self._depth:
            self._depth = depth

        if direction == 'left':
            parent.left = n
        else:
            parent.right = n

        self._size += 1

    def contains(self, value):
        # return true if value in tree, false if not
        if self._head is None:
            return False

        current = self._head
        while current is not None:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True
        return False

    def size(self):
        # return total number of values stored in tree
        return self._size

    def depth(self):
        # return int of total number of tree levels
        return self._depth

    def balance(self):
        # return positive int if more values on left
        # negative if more values on right
        # 0 if balanced
        return self._balance
