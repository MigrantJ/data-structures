class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree():
    def __init__(self):
        pass
    
    def insert(self, value):
        # insert value into tree. if already present, ignored
        pass

    def contains(self, value):
        # return true if value in tree, false if not
        pass

    def size(self):
        # return total number of values stored in tree
        pass

    def depth(self):
        # return int of total number of tree levels
        pass

    def balance(self):
        # return positive int if more values on left
        # negative if more values on right
        # 0 if balanced
        pass
