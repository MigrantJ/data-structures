from __future__ import unicode_literals


class HashTable():
    """The hash table is of fixed size.  The number of slots in the table
    are determined when the table is initialized, by passing an
    argument: ``foo = HashTable(1024)`` It handles hash collisions
    by using 'buckets' to contain any values that share a hash.
    It accepts only strings as keys. """
    def __init__(self, size):
        self.size = size
        self.table = []
        for _ in range(size):
            self.table.append([])

    def set(self, key, val):
        """If a non-string is provided, the 'set' method should raise an
        appropriate Python exception. Should store the given val using the
        given key"""
        if type(key) is not str and key != "":
            raise TypeError('You must pass a string that is not empty as key.')
        count = 0
        for item in self.table[self.hash(key)]:
            if item[0] == key:
                item[1] = val
                count = 1
        if count is not 1:
            self.table[self.hash(key)].append([key, val])

    def get(self, key):
        """should return the value stored with the given key"""
        for item in self.table[self.hash(key)]:
            if item[0] == key:
                return item[1]

    def hash(self, key):
        """should hash the key provided"""
        return reduce(lambda x, y: x+y, [ord(a) for a in key]) % self.size

    def __repr__(self):
        return str(self.table)
